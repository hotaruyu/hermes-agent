---
type: source
title: "2026-07-12 karpathy llm-wiki gist"
description: "> The wiki is a persistent, compounding artifact."
status: active
created: 2026-07-12
updated: 2026-07-12
tags:
  - source
  - karpathywiki
source: karpathywiki
legacy_path: "04_Sources/2026-07-12_karpathy_llm-wiki_gist.md"
---

# 2026-07-12 karpathy llm-wiki gist

## Source
- Title: llm-wiki
- Author: Andrej Karpathy
- URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Date added: 2026-07-12

## 要点
- RAG のように毎回検索して答えるのではなく、LLM が永続的な Wiki を育てる
- 新しい資料が来たら、既存の知識ページへ統合・更新する
- Wiki は相互リンクされた Markdown の集合として管理する
- 人間は資料収集と問いの設定を担当し、LLM は要約・整理・保守を担当する
- Obsidian を閲覧・編集の中心に据える運用が想定されている

## 抜き出した核となる考え
> The wiki is a persistent, compounding artifact.

知識をその場で使い捨てるのでなく、次回以降も使える形に変換して残していくのが核心。

## 反映先
- [LLM Wiki](../topics/hermes/LLM Wiki.md)
- [RAGとの違い](../topics/hermes/RAGとの違い.md)
- [Andrej Karpathy](../topics/hermes/entities/Andrej Karpathy.md)

## 次に考えること
- 自分の資料投入ルール
- ページ命名規則
- 引用の残し方
- 更新ログの粒度
