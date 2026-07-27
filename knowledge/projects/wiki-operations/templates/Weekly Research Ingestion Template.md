---
type: project
title: "Weekly Research Ingestion Template"
description: "週次のKANBAN調査結果を、KarpathyWikiへ同じ形で取り込むためのテンプレート。"
status: active
created: 2026-07-27
updated: 2026-07-27
tags:
  - project
  - karpathywiki
source: karpathywiki
legacy_path: "99_Templates/Weekly Research Ingestion Template.md"
---

# Weekly Research Ingestion Template

週次のKANBAN調査結果を、KarpathyWikiへ同じ形で取り込むためのテンプレート。

---

## 0. 今回の入力
- 週: `{{week-range}}`
- テーマ: `{{theme}}`
- 元レポート: `{{report-path}}`
- 関連分析ファイル:
  - `{{analysis-file-1}}`
  - `{{analysis-file-2}}`
- 取り込み日: `{{date-added}}`
- 対象市場: `{{markets}}`
- 条件: `{{conditions}}`

---

## 1. 作るファイル

### Source
- `04_Sources/{{date-slug}}_{{source-slug}}.md`

### Topics
- `02_Topics/{{topic-1}}.md`
- `02_Topics/{{topic-2}}.md`
- 必要なら `02_Topics/{{topic-3}}.md`

### 更新対象
- `00_Index.md`
- `01_Maps/Knowledge Map.md`
- `05_Logs/Ingestion Log.md`

---

## 2. Sourceページひな形

```md
# {{date-slug}} {{source-title-short}}

## Source
- Title: {{source-title}}
- Author: {{author}}
- Date added: {{date-added}}
- 追記日: {{date-added}}
- Original file: `{{report-path}}`
- Related files:
  - `{{analysis-file-1}}`
  - `{{analysis-file-2}}`
- Scope: {{scope}}
- Conditions: {{conditions}}

## 要点
- 
- 
- 

## 更新履歴
- {{date-added}}: 初回追加

## 重要な観察
### 日本市場
- 

### 米国市場
- 

## {{audience}}向けへの示唆
- 
- 
- 

## 反映先
- {{topic-1}}
- {{topic-2}}

## 次に考えること
- 
- 
- 
```

---

## 3. Topicページひな形（比較系）

```md
# {{topic-1}}

> 追記日: {{date-added}}

## 定義

## 要点
- 
- 
- 

## 更新履歴
- {{date-added}}: 初回追加

## 市場別メモ
### 日本市場
- 

### 米国市場
- 

## 比較
### 共通点
- 
- 

### 相違点
- 
- 

## 企画化の示唆
- 
- 
- 

## 関連
- {{related-topic-1}}
- {{related-topic-2}}
- {{date-slug}}_{{source-slug}}

## 根拠 / 出典
- {{date-slug}}_{{source-slug}}
```

---

## 4. Topicページひな形（視聴者/用途別）

```md
# {{topic-2}}

> 追記日: {{date-added}}

## 定義

## 要点
- 
- 
- 

## 更新履歴
- {{date-added}}: 初回追加

## 刺さりやすい評価軸
### 1. 不安軽減・整理型
- 

### 2. 仕事・会社・定年後への接続
- 

### 3. 生活改善・身近な実用
- 

### 4. 初心者導入性
- 

### 5. 経験価値の肯定
- 

### 6. ニュース理解・社会変化
- 

### 7. すぐ試せる小さな成果
- 

## 今回の調査から見えたこと
- 
- 
- 

## 企画化メモ
- 良い入口: 
- 避けたい入口: 
- 使いやすい核: 

## 関連
- {{topic-1}}
- {{date-slug}}_{{source-slug}}

## 根拠 / 出典
- {{date-slug}}_{{source-slug}}
```

---

## 5. Ingestion Log追記テンプレ

```md
## {{date-added}}
### 追加ソース
- {{date-slug}}_{{source-slug}}

### 作成・更新ページ
- {{topic-1}}
- {{topic-2}}
- [Knowledge Map](../../../maps/knowledge-map.md)

### メモ
{{one-line-summary}}
```

---

## 6. Index / Map 更新ルール

### 00_Index.md
- 入口に新しいTopicとSourceを追加する
- 「今の状態」を1行だけ更新する

### 01_Maps/Knowledge Map.md
- 中心テーマに今回のTopicを追加する
- ソース一覧に今回のSourceを追加する
- 今後増やす枝があれば2個まで追加する

---

## 7. 運用ルール
- 1週につき Source は基本1本にまとめる
- Topic は 2本までに絞る
- 長いレポートでも、Wiki側は「再利用できる結論」を優先する
- 動画タイトル一覧の丸写しより、比較・示唆・翻訳を残す
- 専門用語は必要なら日常語に言い換える
- 次週と比較できるよう、条件や期間は必ず残す
- その日に新規追加・追記した内容には、本文内で見える追記日を残す

---

## 8. 最低限チェック
- [ ] Source に元ファイルパスがある
- [ ] Topic から Source へリンクしている
- [ ] Index に追加した
- [ ] Knowledge Map に追加した
- [ ] Ingestion Log に追記した
- [ ] 次週と比較できる条件・期間が残っている
- [ ] その日追加した内容に追記日が入っている
