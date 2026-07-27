---
type: topic
title: "RAGとの違い"
description: "RAG は「検索して答える」仕組み。 LLM Wiki は「知識を育ててから使う」仕組み。"
status: active
created: 2026-07-12
updated: 2026-07-12
tags:
  - topic
  - karpathywiki
source: karpathywiki
legacy_path: "02_Topics/RAGとの違い.md"
---

# RAGとの違い

## 一般的なRAG
- 資料を保存する
- 質問時に関連チャンクを検索する
- その場で回答を作る

## LLM Wiki
- 資料を読んだ段階で知識を整理する
- 既存ページに統合する
- 相互リンクや論点整理を残す
- 次回以降は蓄積済みの知識を土台に考えられる

## 違いの本質
RAG は「検索して答える」仕組み。
LLM Wiki は「知識を育ててから使う」仕組み。

## LLM Wikiの利点
- 毎回同じ再発見をしなくてよい
- 複数資料の統合結果が残る
- 矛盾・保留点を明示しやすい
- 人間があとで読んでも使いやすい

## 注意点
- 更新ルールがないと散らかる
- 出典を省くと信頼性が落ちる
- 要約の誤りを定期確認する必要がある

## 関連
- [LLM Wiki](LLM Wiki.md)
- [2026-07-12_karpathy_llm-wiki_gist](../../sources/2026-07-12_karpathy_llm-wiki_gist.md)
