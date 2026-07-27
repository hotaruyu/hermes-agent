# KarpathyWiki → OKF → GitHub 移行方針

更新日: 2026-07-27

## 目的

現在、Obsidian/iCloud 上にある KarpathyWiki のメモを、内容を失わずに OKF 準拠 Markdown へ段階的に整理し、GitHub を正本として扱える構成へ移行する。

現行 Wiki ルート:

`C:\Users\hotar\iCloudDrive\iCloud~md~obsidian\MyBrain_iCloud\04_AI\KarpathyWiki`

現行の主な構造:

- `00_Index.md`
- `01_Maps/Knowledge Map.md`
- `02_Topics/`
- `04_Sources/`
- `05_Logs/Ingestion Log.md`

確認済みの既存メモ例:

- `02_Topics/Antigravityによる昭和AI・Google Vidsナレーション制作自動化.md`
- `04_Sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md`
- `02_Topics/GitHub Issue経由のKarpathyWiki取り込み.md`
- `04_Sources/2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c.md`
- `02_Topics/LLM Wiki.md`

## 移行後の役割

- KarpathyWiki: 知識の論理構造・名称
- OKF: Markdown とメタデータの共通形式
- GitHub: 正本、履歴、AI エージェント間の共有先
- Obsidian: 必要な場合のみ閲覧・編集 UI として利用
- Notion: 制作進捗や一覧など、人間向け管理画面に限定

## 移行後の推奨構造

```text
knowledge/
├── index.md
├── maps/
│   └── knowledge-map.md
├── topics/
│   ├── showa-ai/
│   ├── ai-research/
│   ├── vids-automation/
│   ├── antigravity/
│   └── hermes/
├── sources/
├── projects/
└── logs/
    └── ingestion-log.md
```

## OKF メタデータ方針

各 Markdown の先頭に YAML frontmatter を付与する。

最低限の推奨項目:

```yaml
---
type: topic
title: ページタイトル
description: ページの要約
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - ai
source: karpathywiki
---
```

`type` の推奨値:

- `index`
- `map`
- `topic`
- `source`
- `project`
- `log`

## 分類方針

### 昭和AI

YouTube 企画、台本の論点、番宣、調査結果をまとめる。ただし完成台本そのものは既存の `showa-ai-youtube-scripts` を正本とし、KarpathyWiki 側では要約とリンクを保持する。

### AIリサーチ

BCG/HBS の AI 生産性研究、政府の AI 政策、リスキリング、Physical AI、AI 詐欺、sandbagging など、昭和AIの企画に再利用できる調査知識を保持する。

### Vids自動化

Google Vids のシーン追加、ナレーション自動流し込み、Chrome拡張、制作自動化の知見を保持する。

### AntiGravity

複数エージェントを使った昭和AI制作や Google Vids 自動化の設計・検証記録を保持する。

### Hermes

KANBAN、GitHub Issue 受け渡し、ChatGPT → Hermes → KarpathyWiki の取り込み仕様と検証記録を保持する。

## 移行ルール

1. 元ファイルは削除しない。
2. 最初はコピー移行し、内容一致を確認後に旧ファイルを archive 扱いにする。
3. 同じ内容のメモは統合し、元ファイルへの参照を `aliases` または本文末尾に残す。
4. 台本、コード、一次資料はそれぞれ既存の専用 GitHub リポジトリを正本とし、Wiki には複製しない。
5. Wiki 内のページは標準 Markdown リンクを優先し、Obsidian 固有記法への依存を減らす。
6. AI が読むための `description` を各ページに付ける。
7. 出典があるページは本文に URL または GitHub リンクを残す。
8. `index.md` と `maps/knowledge-map.md` から主要ページへ到達できる状態を保つ。

## 移行手順

### Phase 1: 棚卸し

- KarpathyWiki 全 Markdown を一覧化
- 重複タイトル、孤立ページ、リンク切れを検出
- `topic/source/project/log/map/index` に分類

### Phase 2: OKF 化

- YAML frontmatter を付与
- タイトルと説明を標準化
- Obsidian 固有リンクを可能な範囲で標準 Markdown 化

### Phase 3: GitHub 正本化

- `knowledge/` 以下へ配置
- インデックスと Knowledge Map を再構築
- GitHub 上の既存リポジトリへの参照を整理

### Phase 4: 自動取り込み更新

既存の ChatGPT → GitHub Issue → Hermes → KarpathyWiki の取り込み先を、GitHub の `knowledge/` OKF 構造へ変更する。

新規メモは原則として最初から OKF frontmatter を付け、適切な `topics/` または `sources/` へ保存する。

## 完了条件

- 既存メモが失われていない
- 全主要 Markdown に OKF メタデータがある
- `index.md` から主要テーマへ辿れる
- 重複メモが整理されている
- GitHub を正本として ChatGPT / Hermes / Claude / Codex / AntiGravity が同じ知識を参照できる
- Obsidian や Notion がなくても知識ベース自体は成立する
