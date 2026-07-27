---
type: log
title: "KarpathyWiki Migration Status"
description: "旧KarpathyWikiからknowledge/への移行進捗ログ。"
status: active
created: 2026-07-27
updated: 2026-07-27
tags:
  - log
  - migration
  - karpathywiki
source: karpathywiki
---

# KarpathyWiki Migration Status

- migrated_pages: 44
- last_run: 2026-07-27
- policy: copy-only migration; legacy wiki remains untouched.

## Completed
- Full Markdown inventory completed.
- YAML frontmatter normalized for migrated pages.
- Obsidian wikilinks converted to standard Markdown links where targets were found.
- `knowledge/index.md` and `knowledge/maps/knowledge-map.md` regenerated.

## Remaining manual review
- Review duplicate/merge candidates in `migration-report.md`.
- Verify canonical GitHub links for summarized script pages if a more precise repo path becomes available.

## Safety
- Source vault was not modified or deleted.
