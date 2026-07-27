from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "karpathywiki_migrate.py"
spec = importlib.util.spec_from_file_location("karpathywiki_migrate", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_replace_obsidian_links_handles_vault_root_and_parent_links() -> None:
    source_to_dest = {
        Path("02_Topics/Topic A.md"): Path("topics/showa-ai/Topic A.md"),
        Path("04_Sources/Source A.md"): Path("sources/Source A.md"),
    }
    source_lookup = {
        "topic a": Path("02_Topics/Topic A.md"),
        "source a": Path("04_Sources/Source A.md"),
    }

    converted, broken, resolved = module.replace_obsidian_links(
        "See [[../04_Sources/Source A]] and [[Topic A|topic]].",
        Path("02_Topics/Topic A.md"),
        source_to_dest,
        source_lookup,
    )

    assert "[Source A](../../sources/Source A.md)" in converted
    assert "[topic](Topic A.md)" in converted
    assert broken == []
    assert Path("04_Sources/Source A.md") in resolved
    assert Path("02_Topics/Topic A.md") in resolved


def test_build_theme_index_uses_relative_links_for_nested_pages() -> None:
    page = module.Page(
        source_path=Path("03_Entities/Andrej Karpathy.md"),
        rel_source=Path("03_Entities/Andrej Karpathy.md"),
        title="Andrej Karpathy",
        heading="Andrej Karpathy",
        body="# Andrej Karpathy\n",
        raw_text="# Andrej Karpathy\n",
        file_type="topic",
        theme="hermes",
        dest_rel=Path("topics/hermes/entities/Andrej Karpathy.md"),
        created="2026-07-27",
        updated="2026-07-27",
        tags=["karpathywiki"],
    )

    text = module.build_theme_index("2026-07-27", "hermes", [page])

    assert "[Andrej Karpathy](entities/Andrej Karpathy.md)" in text
