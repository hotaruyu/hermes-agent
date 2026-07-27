---
type: source
title: "2026-07-12 showa ai channel concept excerpt"
description: "Migrated from legacy KarpathyWiki: 04_Sources/2026-07-12_showa-ai-channel-concept-excerpt.md"
status: active
created: 2026-07-12
updated: 2026-07-12
tags:
  - source
  - karpathywiki
source: karpathywiki
legacy_path: "04_Sources/2026-07-12_showa-ai-channel-concept-excerpt.md"
---

# 2026-07-12 showa ai channel concept excerpt

## Source
- Title: 昭和AI チャンネルコンセプト / 制作運用メモ（抜粋）
- Author: ユーザー管理のNotion/Claude artifact由来メモ
- Date added: 2026-07-12
- Source type: pasted excerpt in Hermes chat
- Original source note: Claude公開Artifactの本文取得はCloudflareで失敗したため、ユーザー貼り付け部分のみを根拠として登録
- Scope: 制作ツール構成 / 制作進捗管理 / 未着手アクションの断片

## 要点
- 制作ワークフローは、ナレーション、進捗管理、画像生成、B-roll、ソース管理で役割分担されている。
- VOICEVOX は台本ナレーションの読み上げ用整形先として使う。
- Notion は制作進捗管理の中核で、7章の知見参照先でもある。
- Python/PIL はサムネイルやSNS画像のコード描画に使う。
- image2 / Veo 3 は情感的なB-roll補助に限定し、正確性が必要な図や数字はRemotion側で描く。
- NotebookLM はチャンネルのソースドキュメント管理に使う。

## 制作運用ルールとして読み取れること
- AI生成画像は主役ではなく補助的な使い方に限定する。
- 正確な図解や数字は、編集・描画側でコントロール可能な手段を優先する。
- 進捗の正本はNotion DBであり、要約ドキュメント単体を最新状態と見なしてはいけない。

## 未着手タスク（抜粋）
- 動画 #13（AARP回）と #15（経験は抽象化されて〜回）のRemotion本編制作
- #15用サムネイルの最終決定
- 「テーマ・アイデア一覧」にある20本ブレストのうち、DB未登録18本の採番・登録
- Remotionプロジェクト一式(zip)の外部保管とNotionからのリンク化

## 制約 / 注意
- これはチャンネルコンセプト全文ではなく抜粋である。
- 最新の制作状況はNotionの制作管理DBで確認する前提。
- 着手前にNotionの現在ステータス確認が必要、という運用ルールが明示されている。

## 反映先
- [昭和AI チャンネル運用ルール](../topics/antigravity/昭和AI チャンネル運用ルール.md)
- [昭和世代に響くAI動画の特徴](../topics/showa-ai/昭和世代に響くAI動画の特徴.md)

## 次に考えること
- Notion本文全体を取得できたら、チャンネル思想・NG表現・成功条件を追記する。
- 制作ツール構成を「制作パイプライン」として独立ページ化するか検討する。
- 未着手タスクをKarpathyWikiではなく制作管理系にどう橋渡しするか整理する。
