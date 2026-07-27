---
type: project
title: "Hermes用 Obsidian反映指示"
description: "以下を Hermes にそのまま渡して使う。"
status: active
created: 2026-07-27
updated: 2026-07-27
tags:
  - project
  - karpathywiki
source: karpathywiki
legacy_path: "98_Handoffs/2026-07-14_Hermes用_Obsidian反映指示.md"
---

# Hermes用 Obsidian反映指示

以下を Hermes にそのまま渡して使う。

---

Obsidian vault の次の場所を作業対象にしてください。

- `C:\Users\hotar\iCloudDrive\iCloud~md~obsidian\MyBrain_iCloud\04_AI\KarpathyWiki\`

## 目的
Claude が作った整理案や Markdown 案を、Obsidian 内へ安全に反映したいです。

## ルール
- 既存ノートを尊重する
- 勝手な大規模再編成はしない
- まず現状確認をしてから、最小変更で進める
- 変更前に、何を変えるかを短く示す
- Markdown 形式を保つ
- Obsidian の内部リンクは `ノート名` を使う
- 新規作成ページと既存ページへの追記には、本文内で判別できる形の追記日（例: `追記日: 2026-07-27` / `更新履歴`）を残す

## 優先作業
1. `00_Index.md` を入口として確認する
2. 関連する既存ノートを読む
3. Claude の案に沿って、必要なノートを更新または作成する
4. `05_Logs/Ingestion Log.md` に必要なら反映ログを追記する
5. 変更後に、更新したファイル一覧を短く報告する
6. その日追加した内容には追記日を残したか確認する

## 主な保存先ルール
- `02_Topics/` = テーマ整理
- `03_Entities/` = 人物・サービス・概念
- `04_Sources/` = 元資料・抜粋・調査メモ
- `05_Logs/` = 反映履歴
- `98_Handoffs/` = 引き継ぎメモ・作業指示

## 依頼時の入力形式
私が Claude の出力を渡したら、次の順で処理してください。
- どのファイルを作る/更新するか確認
- 必要なら既存ノートとの重複確認
- 実ファイルへ反映
- 反映結果を短く報告

## 最初に返す内容
最初に次だけ短く返してください。
1. 今回読むべきノート
2. 更新候補ファイル
3. 新規作成候補ファイル
