---
type: topic
title: "GitHub Issue経由のKarpathyWiki取り込み"
description: "ChatGPT など別の作業場所で整理した知識を、GitHub Issue を中継点にして Hermes が Obsidian 内の KarpathyWiki へ反映する運用パターン。"
status: active
created: 2026-07-25
updated: 2026-07-25
tags:
  - topic
  - karpathywiki
source: karpathywiki
legacy_path: "02_Topics/GitHub Issue経由のKarpathyWiki取り込み.md"
---

# GitHub Issue経由のKarpathyWiki取り込み

## 定義
ChatGPT など別の作業場所で整理した知識を、GitHub Issue を中継点にして Hermes が Obsidian 内の KarpathyWiki へ反映する運用パターン。

## 確認済み事項
- 手動テストでは、ChatGPT から KarpathyWiki へ知識を渡すブリッジとして GitHub Issue を使う想定が確認されている。
- 取り込み先の KarpathyWiki は Obsidian vault 配下で運用されている。
- 取り込み時は、既存ページとの重複回避、Source / Topic / Log 更新、provenance 保持が重要である。

## この運用で大事なこと
- GitHub Issue は知識の最終保管先ではなく、中継点として扱う。
- 反映時は新規ページ乱立より、既存 Topic への統合を優先する。
- テスト用の小さな知識でも、出典 URL と更新ログを残しておくと後で検証しやすい。

## 使いどころ
- ChatGPT 側で作った整理結果を、そのまま消さずに Obsidian へ移したいとき。
- Claude / ChatGPT / Hermes の役割を分けつつ、最終的な知識を 1つの Wiki に寄せたいとき。
- 「会話」ではなく「残る Markdown」を正本寄りに育てたいとき。

## 仮説・アイデア
- 手動テスト段階では Source ページを必ず作る方が provenance を追いやすい。
- 定常運用では、Issue ごとに新規 Topic を作るより、既存の運用ページへ統合する方が保守しやすい可能性がある。
- 取り込み完了後に Issue コメント追加や close まで自動化できると、ブリッジとしての完成度が上がる。

## 未確認 / 要検証
- どの種類の Issue を独立 Source として残し、どの種類を既存運用メモへ統合するのがよいか。
- `00_Index.md` と `01_Maps/Knowledge Map.md` へのリンク追加を、毎回の必須ルールにするか。
- GitHub Issue コメント追加と close を Hermes 運用の標準フローに含めるか。

## 関連
- [LLM Wiki](LLM Wiki.md)
- [RAGとの違い](RAGとの違い.md)
- [hermes-claude-shared-wiki-ops](../../projects/wiki-operations/handoffs/hermes-claude-shared-wiki-ops.md)
- [2026-07-14_Hermes用_Obsidian反映指示](../../projects/wiki-operations/handoffs/2026-07-14_Hermes用_Obsidian反映指示.md)
- [2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c](../../sources/2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c.md)

## 根拠 / 出典
- [2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c](../../sources/2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c.md)
- https://github.com/hotaruyu/hermes-agent/issues/2
