---
type: project
title: "Claude-Hermes共有運用メモ"
description: "作成日: 2026-07-14 目的: Obsidian を Claude と Hermes の共通作業場として使うための最小ルールを固定する。"
status: active
created: 2026-07-14
updated: 2026-07-14
tags:
  - project
  - karpathywiki
source: karpathywiki
legacy_path: "98_Handoffs/2026-07-14_Claude-Hermes共有運用メモ.md"
---

# Claude-Hermes共有運用メモ

作成日: 2026-07-14  
目的: Obsidian を Claude と Hermes の共通作業場として使うための最小ルールを固定する。

---

## 基本方針
- 共有するのは **会話履歴** ではなく **Obsidian の Markdown ノート**
- Claude は **整理案・要約・本文案作成** を主に担当
- Hermes は **実ファイル反映・更新・継続運用** を主に担当
- いきなり全体再編せず、**小さく提案して小さく反映** する

## 共通作業場所
- `C:\Users\hotar\iCloudDrive\iCloud~md~obsidian\MyBrain_iCloud\04_AI\KarpathyWiki\`

## 役割分担
### Claude
- ノートの要約
- 重複整理案
- 新規ノート案
- `内部リンク` 候補
- Markdown 本文案の作成

### Hermes
- 既存ノート確認
- 実ファイルの作成/更新
- フォルダ整合性の維持
- 反映ログ管理
- 将来の定期運用への接続

## 使い方
1. Claude に対象ノートまたは要件を渡す
2. Claude から `ファイル名 / 保存先 / 本文案` を受け取る
3. その出力を Hermes に渡す
4. Hermes が既存ノートを確認して最小変更で反映する
5. 必要なら `05_Logs/Ingestion Log.md` に反映を残す

## 保存場所の基本ルール
- `00_Index.md` = 入口
- `01_Maps/` = 全体関係
- `02_Topics/` = トピック整理
- `03_Entities/` = 人物・サービス・概念
- `04_Sources/` = 元資料・引用・調査メモ
- `05_Logs/` = 履歴
- `98_Handoffs/` = 引き継ぎ・指示文

## 実務ルール
- 1回の変更は小さくする
- 変更前に対象ファイルを確認する
- 既存内容を壊しそうな場合は、先に候補案だけ出す
- 不明点は候補を 2〜3 個に絞る
- 長文説明より、コピペできる本文案を優先する

## 次に使うファイル
- [2026-07-14_Claude用_Obsidian共有プロンプト](2026-07-14_Claude用_Obsidian共有プロンプト.md)
- [2026-07-14_Hermes用_Obsidian反映指示](2026-07-14_Hermes用_Obsidian反映指示.md)
