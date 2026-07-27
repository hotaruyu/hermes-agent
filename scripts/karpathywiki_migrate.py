from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

DEFAULT_SOURCE_ROOT = Path(r"C:\Users\hotar\iCloudDrive\iCloud~md~obsidian\MyBrain_iCloud\04_AI\KarpathyWiki")
DEFAULT_DEST_ROOT = Path("knowledge")
CANONICAL_SCRIPT_LINKS = {
    "昭和AI 3本目台本_AI導入と生産性のJカーブ.md": "https://github.com/hotaruyu/hotaruyubandai",
    "昭和AI_ep4台本_パソコン登場とAI普及の法則.md": "https://github.com/hotaruyu/hotaruyubandai",
}
THEME_RULES = [
    ("hermes", ["hermes", "github issue", "karpathywiki", "llm wiki", "wiki"]),
    ("antigravity", ["antigravity"]),
    ("vids-automation", ["vids", "video", "narration", "ナレーション", "google vids"]),
    ("showa-ai", ["昭和ai", "昭和世代", "showa ai", "台本"]),
    ("ai-research", ["llm", "rag", "research", "youtubeトレンド", "trend", "research"]),
]


@dataclass
class Page:
    source_path: Path
    rel_source: Path
    title: str
    heading: str
    body: str
    raw_text: str
    file_type: str
    theme: str | None
    dest_rel: Path
    created: str
    updated: str
    tags: list[str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    frontmatter_text = parts[0][4:]
    body = parts[1]
    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in frontmatter_text.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(line[4:].strip().strip('"'))
            continue
        if ":" not in line:
            current_list_key = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        current_list_key = None
        data[key] = value.strip().strip('"')
    return data, body


def extract_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def first_paragraph(body: str) -> str:
    lines: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if line.startswith("#"):
            continue
        if line.startswith("-") or line.startswith("```"):
            continue
        lines.append(line)
        if sum(len(x) for x in lines) > 180:
            break
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:160] if len(text) > 160 else text


def normalize_for_compare(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\.md$", "", value)
    value = re.sub(r"[^\w\u3040-\u30ff\u3400-\u9fff]+", "", value)
    return value


def infer_theme(title: str, body: str, rel_source: Path) -> str | None:
    haystack = " ".join([title, body[:400], str(rel_source)]).lower()
    if rel_source.parts and rel_source.parts[0] in {"98_Handoffs", "99_Templates"}:
        return "hermes"
    for theme, needles in THEME_RULES:
        if any(needle in haystack for needle in needles):
            return theme
    if rel_source.parts and rel_source.parts[0] == "03_Entities":
        return "ai-research"
    if "用途" in title:
        return "ai-research"
    return None


def infer_type(rel_source: Path) -> str:
    if rel_source.name == "00_Index.md":
        return "index"
    top = rel_source.parts[0]
    return {
        "01_Maps": "map",
        "02_Topics": "topic",
        "03_Entities": "topic",
        "04_Sources": "source",
        "05_Logs": "log",
        "98_Handoffs": "project",
        "99_Templates": "project",
    }.get(top, "project")


def destination_for(rel_source: Path, file_type: str, theme: str | None) -> Path:
    name = rel_source.name
    top = rel_source.parts[0]
    if file_type == "index":
        return Path("index.md")
    if file_type == "map":
        slug = "knowledge-map.md" if name == "Knowledge Map.md" else name
        return Path("maps") / slug
    if file_type == "source":
        return Path("sources") / name
    if file_type == "log":
        return Path("logs") / name.replace("Ingestion Log.md", "ingestion-log.md")
    if top == "98_Handoffs":
        return Path("projects") / "wiki-operations" / "handoffs" / name
    if top == "99_Templates":
        return Path("projects") / "wiki-operations" / "templates" / name
    if top == "03_Entities":
        return Path("topics") / (theme or "ai-research") / "entities" / name
    if file_type == "topic":
        return Path("topics") / (theme or "unclassified") / name
    return Path("projects") / (theme or "misc") / name


def format_date(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def yaml_escape(value: str) -> str:
    return value.replace('"', '\\"')


def build_frontmatter(page: Page, description: str) -> str:
    tags = [page.file_type, "karpathywiki", *page.tags]
    deduped_tags: list[str] = []
    seen = set()
    for tag in tags:
        if not tag:
            continue
        if tag not in seen:
            seen.add(tag)
            deduped_tags.append(tag)
    lines = [
        "---",
        f'type: {page.file_type}',
        f'title: "{yaml_escape(page.title)}"',
        f'description: "{yaml_escape(description)}"',
        "status: active",
        f'created: {page.created}',
        f'updated: {page.updated}',
        "tags:",
    ]
    for tag in deduped_tags:
        lines.append(f"  - {tag}")
    lines.append("source: karpathywiki")
    lines.append("legacy_path: \"" + yaml_escape(str(page.rel_source).replace('\\', '/')) + "\"")
    lines.append("---")
    return "\n".join(lines)


def iter_markdown_files(source_root: Path) -> Iterable[Path]:
    for path in sorted(source_root.rglob("*.md")):
        if path.is_file():
            yield path


def load_pages(source_root: Path) -> list[Page]:
    pages: list[Page] = []
    for path in iter_markdown_files(source_root):
        rel_source = path.relative_to(source_root)
        raw_text = read_text(path)
        frontmatter, body = split_frontmatter(raw_text)
        heading = extract_heading(body)
        title = str(frontmatter.get("title") or heading or path.stem)
        file_type = infer_type(rel_source)
        theme = infer_theme(title, body, rel_source) if file_type in {"topic", "project"} else None
        stat = path.stat()
        created = str(frontmatter.get("created") or format_date(stat.st_mtime))[:10]
        updated = str(frontmatter.get("updated") or format_date(stat.st_mtime))[:10]
        raw_tags = frontmatter.get("tags") if isinstance(frontmatter.get("tags"), list) else []
        tags = [str(tag) for tag in raw_tags]
        pages.append(
            Page(
                source_path=path,
                rel_source=rel_source,
                title=title,
                heading=heading,
                body=body,
                raw_text=raw_text,
                file_type=file_type,
                theme=theme,
                dest_rel=destination_for(rel_source, file_type, theme),
                created=created,
                updated=updated,
                tags=tags,
            )
        )
    return pages


def replace_obsidian_links(
    body: str,
    source_rel: Path,
    source_to_dest: dict[Path, Path],
    source_lookup: dict[Path, Page],
) -> tuple[str, list[str], list[Path]]:
    broken: list[str] = []
    resolved_targets: list[Path] = []

    def replacer(match: re.Match[str]) -> str:
        inner = match.group(1).strip()
        target_part, alias = (inner.split("|", 1) + [None])[:2] if "|" in inner else (inner, None)
        target_part = target_part.split("#", 1)[0].strip()
        if not target_part:
            return match.group(0)
        normalized_target = target_part.replace("\\", "/")
        parts = Path(normalized_target)
        if normalized_target.startswith("/"):
            resolved = Path(normalized_target.lstrip("/"))
        elif parts.parts and parts.parts[0] in {"00_Index.md", "01_Maps", "02_Topics", "03_Entities", "04_Sources", "05_Logs", "98_Handoffs", "99_Templates"}:
            resolved = parts
        elif len(parts.parts) >= 2 and parts.parts[0] == ".." and parts.parts[1] in {"01_Maps", "02_Topics", "03_Entities", "04_Sources", "05_Logs", "98_Handoffs", "99_Templates"}:
            resolved = Path(*parts.parts[1:])
        else:
            base = source_rel.parent
            resolved = (base / normalized_target).resolve().relative_to(Path.cwd().anchor) if False else None
            resolved = Path(os.path.normpath(str(base / normalized_target)))
        if resolved.suffix.lower() != ".md":
            resolved = resolved.with_suffix(".md")
        resolved_parts = Path(*resolved.parts)
        text = (alias or Path(target_part).stem).strip()
        if resolved_parts in source_to_dest:
            resolved_targets.append(resolved_parts)
            dest_rel = source_to_dest[resolved_parts]
            current_dest = source_to_dest[source_rel]
            rel_link = os.path.relpath(dest_rel, start=current_dest.parent).replace("\\", "/")
            return f"[{text}]({rel_link})"

        broken.append(normalized_target)
        return text

    converted = re.sub(r"\[\[([^\]]+)\]\]", replacer, body)
    return converted, broken, resolved_targets


def maybe_summarize_script_page(page: Page, body: str) -> str:
    canonical = CANONICAL_SCRIPT_LINKS.get(page.rel_source.name)
    if not canonical:
        return body
    legacy_path = str(page.rel_source).replace("\\", "/")
    summary_lines = [
        f"# {page.title}",
        "",
        "> 注: 完成台本の正本は専用リポジトリ側を参照し、このページには要約のみを保持する。",
        "",
        f"- 正本候補: {canonical}",
        f"- 旧保管場所: `{legacy_path}`",
        "",
    ]
    sections = []
    current = []
    for line in body.splitlines():
        if line.startswith("## ") and current:
            sections.append(current)
            current = [line]
        else:
            current.append(line)
    if current:
        sections.append(current)
    keep_headers = {"## この台本の位置づけ", "## 関連", "## 📌 校正完了チェックリスト"}
    kept_any = False
    for section in sections:
        if not section:
            continue
        header = section[0].strip()
        if header in keep_headers:
            kept_any = True
            summary_lines.extend(section)
            summary_lines.append("")
        elif header.startswith("## 🎬"):
            kept_any = True
            summary_lines.extend(["## 要約", "- フルシナリオ本文は正本リポジトリで管理する。", "- このノートでは構成意図・再利用ポイント・関連知識への導線のみ残す。", ""])
    if not kept_any:
        summary_lines.extend(["## 要約", first_paragraph(body) or "旧KarpathyWikiの完成台本ページ。", ""])
    return "\n".join(summary_lines).strip() + "\n"


def write_page(dest_root: Path, page: Page, content: str) -> None:
    path = dest_root / page.dest_rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def build_index(today: str, pages: list[Page]) -> str:
    topics_by_theme: dict[str, list[Page]] = defaultdict(list)
    sources: list[Page] = []
    projects: list[Page] = []
    logs: list[Page] = []
    for page in pages:
        if page.file_type == "topic":
            topics_by_theme[page.theme or "unclassified"].append(page)
        elif page.file_type == "source":
            sources.append(page)
        elif page.file_type == "project":
            projects.append(page)
        elif page.file_type == "log":
            logs.append(page)
    lines = [
        "---",
        "type: index",
        'title: "KarpathyWiki Knowledge Index"',
        'description: "旧KarpathyWikiをOKF準拠で再編したGitHub正本インデックス。"',
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        "  - index",
        "  - karpathywiki",
        "source: karpathywiki",
        "---",
        "",
        "# KarpathyWiki Knowledge Index",
        "",
        "- [Knowledge Map](maps/knowledge-map.md)",
        "- [Migration Report](logs/migration-report.md)",
        "- [Migration Status](logs/migration-status.md)",
        "",
        "## 主要テーマ",
    ]
    for theme in ["showa-ai", "ai-research", "vids-automation", "antigravity", "hermes"]:
        theme_pages = sorted(topics_by_theme.get(theme, []), key=lambda p: p.title)
        lines.append(f"### {theme}")
        if not theme_pages:
            lines.append("- (no pages)")
        for page in theme_pages:
            lines.append(f"- [{page.title}]({page.dest_rel.as_posix()})")
        lines.append("")
    if projects:
        lines.extend(["## Projects / Operations", *[f"- [{p.title}]({p.dest_rel.as_posix()})" for p in sorted(projects, key=lambda p: p.title)], ""])
    if sources:
        lines.extend(["## Sources", *[f"- [{p.title}]({p.dest_rel.as_posix()})" for p in sorted(sources, key=lambda p: p.title)], ""])
    if logs:
        lines.extend(["## Logs", *[f"- [{p.title}]({p.dest_rel.as_posix()})" for p in sorted(logs, key=lambda p: p.title)], ""])
    return "\n".join(lines).rstrip() + "\n"


def build_map(today: str, pages: list[Page]) -> str:
    topics_by_theme: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        if page.file_type == "topic":
            topics_by_theme[page.theme or "unclassified"].append(page)
    theme_titles = {
        "showa-ai": "昭和AI",
        "ai-research": "AIリサーチ",
        "vids-automation": "Vids自動化",
        "antigravity": "AntiGravity",
        "hermes": "Hermes",
    }
    lines = [
        "---",
        "type: map",
        'title: "Knowledge Map"',
        'description: "旧KarpathyWikiの主要テーマと導線を俯瞰する知識マップ。"',
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        "  - map",
        "  - karpathywiki",
        "source: karpathywiki",
        "---",
        "",
        "# Knowledge Map",
        "",
        "- [Index](../index.md)",
        "",
        "## 中心テーマ",
    ]
    for theme, label in theme_titles.items():
        lines.append(f"### {label}")
        pages_for_theme = sorted(topics_by_theme.get(theme, []), key=lambda p: p.title)
        if not pages_for_theme:
            lines.append("- (no pages)")
        for page in pages_for_theme:
            lines.append(f"- [{page.title}](../{page.dest_rel.as_posix()})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_theme_index(today: str, theme: str, pages: list[Page]) -> str:
    lines = [
        "---",
        "type: index",
        f'title: "{yaml_escape(theme)} topic index"',
        f'description: "{yaml_escape(theme)} 配下に整理したKarpathyWikiノート一覧。"',
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        "  - index",
        f"  - {theme}",
        "  - karpathywiki",
        "source: karpathywiki",
        "---",
        "",
        f"# {theme}",
        "",
        "- [KarpathyWiki Knowledge Index](../../index.md)",
        "",
    ]
    for page in sorted(pages, key=lambda p: p.title):
        rel_link = os.path.relpath(page.dest_rel, start=Path("topics") / theme).replace("\\", "/")
        lines.append(f"- [{page.title}]({rel_link})")
    if not pages:
        lines.append("- (no pages)")
    return "\n".join(lines).rstrip() + "\n"


def build_migration_status(today: str, page_count: int) -> str:
    return "\n".join([
        "---",
        "type: log",
        'title: "KarpathyWiki Migration Status"',
        'description: "旧KarpathyWikiからknowledge/への移行進捗ログ。"',
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        "  - log",
        "  - migration",
        "  - karpathywiki",
        "source: karpathywiki",
        "---",
        "",
        "# KarpathyWiki Migration Status",
        "",
        f"- migrated_pages: {page_count}",
        f"- last_run: {today}",
        "- policy: copy-only migration; legacy wiki remains untouched.",
        "",
        "## Completed",
        "- Full Markdown inventory completed.",
        "- YAML frontmatter normalized for migrated pages.",
        "- Obsidian wikilinks converted to standard Markdown links where targets were found.",
        "- `knowledge/index.md` and `knowledge/maps/knowledge-map.md` regenerated.",
        "",
        "## Remaining manual review",
        "- Review duplicate/merge candidates in `migration-report.md`.",
        "- Verify canonical GitHub links for summarized script pages if a more precise repo path becomes available.",
        "",
        "## Safety",
        "- Source vault was not modified or deleted.",
    ]) + "\n"


def build_report(today: str, pages: list[Page], duplicates: dict[str, list[Page]], broken_links: dict[str, list[str]], inbound_counts: Counter[str], unclassified: list[Page]) -> str:
    type_counts = Counter(page.file_type for page in pages)
    theme_counts = Counter(page.theme or "none" for page in pages if page.file_type in {"topic", "project"})
    orphan_pages = [page for page in pages if inbound_counts[str(page.rel_source)] == 0 and page.file_type not in {"index", "map"}]
    lines = [
        "---",
        "type: log",
        'title: "KarpathyWiki Migration Report"',
        'description: "既存KarpathyWikiの棚卸し、移行結果、リンク検証、重複候補をまとめたレポート。"',
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "tags:",
        "  - log",
        "  - migration",
        "  - report",
        "  - karpathywiki",
        "source: karpathywiki",
        "---",
        "",
        "# KarpathyWiki Migration Report",
        "",
        f"- source_markdown_files: {len(pages)}",
        f"- migrated_pages: {len(pages)}",
        f"- duplicate_title_groups: {len(duplicates)}",
        f"- files_with_broken_links: {sum(1 for items in broken_links.values() if items)}",
        f"- orphan_pages: {len(orphan_pages)}",
        f"- unclassified_pages: {len(unclassified)}",
        "",
        "## Counts by type",
    ]
    for key in ["index", "map", "topic", "source", "project", "log"]:
        lines.append(f"- {key}: {type_counts.get(key, 0)}")
    lines.extend(["", "## Counts by theme"]) 
    for key in ["showa-ai", "ai-research", "vids-automation", "antigravity", "hermes", "none"]:
        lines.append(f"- {key}: {theme_counts.get(key, 0)}")
    lines.extend(["", "## Duplicate / merge candidates"])
    if not duplicates:
        lines.append("- Exact title duplicates: none")
    for normalized, dup_pages in sorted(duplicates.items()):
        lines.append(f"- {normalized}")
        for page in dup_pages:
            lines.append(f"  - {page.rel_source.as_posix()} -> {page.dest_rel.as_posix()}")
    lines.extend(["", "## Broken links"])
    if not any(broken_links.values()):
        lines.append("- none")
    else:
        for rel, items in sorted(broken_links.items()):
            if not items:
                continue
            uniq = sorted(set(items))
            lines.append(f"- {rel}")
            for item in uniq[:10]:
                lines.append(f"  - {item}")
    lines.extend(["", "## Orphan pages (no inbound wiki-links in legacy vault)"])
    for page in sorted(orphan_pages, key=lambda p: p.rel_source.as_posix()):
        lines.append(f"- {page.rel_source.as_posix()} -> {page.dest_rel.as_posix()}")
    lines.extend(["", "## Unclassified pages"])
    if not unclassified:
        lines.append("- none")
    else:
        for page in unclassified:
            lines.append(f"- {page.rel_source.as_posix()}")
    lines.extend([
        "",
        "## Canonicalized pages",
        "- `昭和AI 3本目台本_AI導入と生産性のJカーブ.md` は全文複製を避け、要約＋GitHubリンクへ変換した。",
        "- `昭和AI_ep4台本_パソコン登場とAI普及の法則.md` は全文複製を避け、要約＋GitHubリンクへ変換した。",
    ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate legacy KarpathyWiki markdown into knowledge/.")
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--dest-root", type=Path, default=DEFAULT_DEST_ROOT)
    parser.add_argument("--report-json", type=Path, default=Path("knowledge/logs/migration-report.json"))
    parser.add_argument("--today", default=datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    source_root: Path = args.source_root.resolve()
    dest_root: Path = args.dest_root.resolve()
    today = args.today

    pages = load_pages(source_root)
    source_to_dest = {page.rel_source: page.dest_rel for page in pages}
    source_lookup = {page.rel_source: page for page in pages}

    dest_root.mkdir(parents=True, exist_ok=True)

    broken_links: dict[str, list[str]] = {}
    inbound_counts: Counter[str] = Counter()
    title_groups: dict[str, list[Page]] = defaultdict(list)
    unclassified: list[Page] = []

    for page in pages:
        title_groups[normalize_for_compare(page.title)].append(page)
        if page.file_type in {"topic", "project"} and page.theme is None:
            unclassified.append(page)
        transformed_body = maybe_summarize_script_page(page, page.body)
        transformed_body, broken, resolved_targets = replace_obsidian_links(
            transformed_body,
            page.rel_source,
            source_to_dest,
            source_lookup,
        )
        broken_links[page.rel_source.as_posix()] = broken
        for target in resolved_targets:
            inbound_counts[str(target)] += 1
        description = first_paragraph(transformed_body) or f"Migrated from legacy KarpathyWiki: {page.rel_source.as_posix()}"
        frontmatter = build_frontmatter(page, description)
        content = frontmatter + "\n\n" + transformed_body.strip() + "\n"
        write_page(dest_root, page, content)

    duplicates = {key: value for key, value in title_groups.items() if key and len(value) > 1}

    index_text = build_index(today, pages)
    map_text = build_map(today, pages)
    status_page = build_migration_status(today, len(pages))
    report_text = build_report(today, pages, duplicates, broken_links, inbound_counts, unclassified)

    (dest_root / "index.md").write_text(index_text, encoding="utf-8")
    theme_pages: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        if page.file_type == "topic":
            theme_pages[page.theme or "unclassified"].append(page)
    for theme in ["showa-ai", "ai-research", "vids-automation", "antigravity", "hermes", "unclassified"]:
        theme_dir = dest_root / "topics" / theme
        theme_dir.mkdir(parents=True, exist_ok=True)
        (theme_dir / "index.md").write_text(build_theme_index(today, theme, theme_pages.get(theme, [])), encoding="utf-8")
    (dest_root / "maps").mkdir(parents=True, exist_ok=True)
    (dest_root / "maps" / "knowledge-map.md").write_text(map_text, encoding="utf-8")
    (dest_root / "logs").mkdir(parents=True, exist_ok=True)
    (dest_root / "logs" / "migration-status.md").write_text(status_page, encoding="utf-8")
    (dest_root / "logs" / "migration-report.md").write_text(report_text, encoding="utf-8")

    report_json = {
        "today": today,
        "source_root": str(source_root),
        "dest_root": str(dest_root),
        "source_markdown_files": len(pages),
        "duplicate_title_groups": {key: [page.rel_source.as_posix() for page in value] for key, value in duplicates.items()},
        "broken_links": broken_links,
        "unclassified_pages": [page.rel_source.as_posix() for page in unclassified],
        "pages": [
            {
                "source": page.rel_source.as_posix(),
                "destination": page.dest_rel.as_posix(),
                "type": page.file_type,
                "theme": page.theme,
                "title": page.title,
            }
            for page in pages
        ],
    }
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"migrated_pages": len(pages), "dest_root": str(dest_root), "report": str(dest_root / 'logs' / 'migration-report.md')}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
