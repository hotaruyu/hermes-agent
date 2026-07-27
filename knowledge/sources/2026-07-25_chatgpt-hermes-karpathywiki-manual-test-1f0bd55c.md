---
type: source
title: "2026-07-25 ChatGPT-Hermes-KarpathyWiki 手動テスト 1f0bd55c"
description: "Migrated from legacy KarpathyWiki: 04_Sources/2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c.md"
status: active
created: 2026-07-25
updated: 2026-07-25
tags:
  - source
  - karpathywiki
source: karpathywiki
legacy_path: "04_Sources/2026-07-25_chatgpt-hermes-karpathywiki-manual-test-1f0bd55c.md"
---

# 2026-07-25 ChatGPT-Hermes-KarpathyWiki 手動テスト 1f0bd55c

## Source
- Title: ChatGPT-Hermes-KarpathyWiki 手動テスト 1f0bd55c
- Origin: pasted source material for manual bridge test
- Repository: https://github.com/hotaruyu/hermes-agent
- GitHub Issue provenance: https://github.com/hotaruyu/hermes-agent/issues/2
- Related concept source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Date added: 2026-07-25
- Scope: ChatGPT から Hermes を経由して KarpathyWiki へ知識を手動取り込みするブリッジ運用の試験メモ
- Note: このページは Issue 本文そのものではなく、今回チャットに貼られた source material をもとに整理した要約。

## 確認済み事実
- ChatGPT から KarpathyWiki へ知識を渡すためのブリッジを手動テストしている。
- GitHub Issue を中継点として使い、Hermes が KarpathyWiki に取り込む想定である。
- KarpathyWiki の保存先は Obsidian vault 配下にある。

## 気づき・解釈
- 取り込み時は、既存ページとの重複回避が重要。
- Source / Topic / Log を更新し、導線を崩さないことが重要。
- テスト用の知識でも provenance と更新ログを残すこと自体に価値がある。

## 仮説
- このテスト Issue は、新しい Source ページとして保存されるか、既存の運用メモ系ページに統合される可能性がある。

## 未確認事項
- どの Topic ページに最終的に統合されるか。
- `00_Index.md` と `01_Maps/Knowledge Map.md` に新規リンクが追加されるか。
- Issue へのコメント追加と close が自動で行われるか。

## 今後試すこと
- 1件の手動取り込みを成功させる。
- GitHub Issue へのコメントと close の自動化有無を確認する。

## 反映先
- [GitHub Issue経由のKarpathyWiki取り込み](../topics/hermes/GitHub Issue経由のKarpathyWiki取り込み.md)
- [LLM Wiki](../topics/hermes/LLM Wiki.md)
- [hermes-claude-shared-wiki-ops](../projects/wiki-operations/handoffs/hermes-claude-shared-wiki-ops.md)

## 次に考えること
- ChatGPT → GitHub Issue → Hermes → Obsidian の流れで、どこを正本にするか。
- 手動テストと定常運用で、どこまで同じテンプレートを使えるか。
- 取り込み完了時に残す最小ログ粒度を固定できるか。
