from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[2] / "tools" / "chatgpt_wiki_inbox.py"


def load_module():
    spec = importlib.util.spec_from_file_location("chatgpt_wiki_inbox", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_resolve_skills_prefers_available_karpathywiki_skill(monkeypatch):
    mod = load_module()
    monkeypatch.setattr(
        mod,
        "run",
        lambda cmd, **kwargs: "│ karpathywiki-ingestion │\n│ obsidian-llm-wiki │",
    )

    assert mod.resolve_skills() == ["karpathywiki-ingestion", "obsidian-llm-wiki"]



def test_ensure_repo_supports_issues_raises_when_disabled(monkeypatch):
    mod = load_module()
    monkeypatch.setattr(
        mod,
        "run",
        lambda cmd, **kwargs: json.dumps({"hasIssuesEnabled": False}),
    )

    with pytest.raises(SystemExit, match="Issues are disabled.*enable-issues"):
        mod.ensure_repo_supports_issues("hotaruyu/hermes-agent")



def test_ingest_uses_wiki_root_as_cwd_and_passes_skills(monkeypatch, tmp_path: Path):
    mod = load_module()
    calls: list[tuple[list[str], str | None]] = []

    def fake_run(cmd, **kwargs):
        calls.append((cmd, kwargs.get("cwd")))
        return "OK"

    monkeypatch.setattr(mod, "run", fake_run)
    issue = {
        "title": "[WIKI-INBOX] Test Topic",
        "body": "source body",
        "url": "https://github.com/hotaruyu/hermes-agent/issues/1",
    }

    result = mod.ingest(
        issue,
        repo="hotaruyu/hermes-agent",
        wiki_root=tmp_path,
        skills=["karpathywiki-ingestion", "obsidian-llm-wiki"],
    )

    assert result == "OK"
    cmd, cwd = calls[-1]
    assert cmd[:3] == ["hermes", "--skills", "karpathywiki-ingestion,obsidian-llm-wiki"]
    assert cmd[3] == "-z"
    assert cwd == str(tmp_path)



def test_main_dry_run_prints_matching_issues_json(monkeypatch, capsys, tmp_path: Path):
    mod = load_module()
    monkeypatch.setattr(
        mod,
        "parse_args",
        lambda: argparse.Namespace(
            repo="hotaruyu/hermes-agent",
            wiki_root=str(tmp_path),
            limit=1,
            dry_run=True,
        ),
    )
    monkeypatch.setattr(mod, "preflight", lambda args: (tmp_path, ["karpathywiki-ingestion"]))
    monkeypatch.setattr(
        mod,
        "list_inbox_issues",
        lambda repo, limit: [
            {
                "number": 7,
                "title": "[WIKI-INBOX] Dry Run",
                "url": "https://github.com/hotaruyu/hermes-agent/issues/7",
            }
        ],
    )

    mod.main()

    out = capsys.readouterr().out
    payload = json.loads(out)
    assert payload["repo"] == "hotaruyu/hermes-agent"
    assert payload["wiki_root"] == str(tmp_path)
    assert payload["skills"] == ["karpathywiki-ingestion"]
    assert payload["matching_issue_count"] == 1
    assert payload["matching_issues"][0]["number"] == 7
