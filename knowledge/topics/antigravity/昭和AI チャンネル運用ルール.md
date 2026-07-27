---
type: topic
title: "昭和AI チャンネル運用ルール"
description: "昭和AIチャンネルの制作運用で、どのツールを何に使うか、どの情報を正本とみなすか、AI生成をどこまで使うかを整理したトピック。"
status: active
created: 2026-07-25
updated: 2026-07-25
tags:
  - topic
  - karpathywiki
source: karpathywiki
legacy_path: "02_Topics/昭和AI チャンネル運用ルール.md"
---

# 昭和AI チャンネル運用ルール

## 定義
昭和AIチャンネルの制作運用で、どのツールを何に使うか、どの情報を正本とみなすか、AI生成をどこまで使うかを整理したトピック。

## 要点
- 制作進捗の正本は Notion で管理する。
- ナレーション音声は VOICEVOX を前提に、台本の読み上げ向け整形が必要。
- サムネイルやSNS画像は Python/PIL によるコード描画が使える。
- image2 / Veo 3 は情感的なB-roll補助に限定し、数字や図の正確性が必要なものは Remotion 側で描く。
- NotebookLM はチャンネルのソースドキュメント管理に使う。
- Antigravity + Google Vids によるシーン別ナレーション投入自動化は、制作実行の新候補として仮説段階にある。
- Notionの制作管理DBには、チェックボックス文字列や固定ステータス値など独自運用ルールがある。
- Remotionは Phase完全分離 + `timing.ts` 一元管理の設計で運用されている。

## 運用上の原則
### 1. 正本は Notion
- 制作状況の最終確認先は Notion の制作管理DB。
- 会話要約や抜粋メモは参考情報であり、最新状態そのものではない。

### 2. 読み上げ前提で台本を整える
- ナレーション文は、そのまま読み上げて不自然でない形に整える必要がある。
- 情報密度よりも、音声で聞いたときの理解しやすさを優先する。

### 3. 正確性が必要な図はAI生成に任せすぎない
- グラフ、数字、比較図、タイミングが重要な図解は Remotion 側で描く。
- AI画像生成は雰囲気づくりや背景素材に限定する。

### 4. 制作ツールは役割分担する
- VOICEVOX: ナレーション
- Notion(MCP経由): 進捗と制作管理、7章の知見参照
- Python/PIL: サムネイル・SNS画像
- image2 / Veo 3: B-roll補助
- NotebookLM: ソース管理
- Remotion(React+TypeScript): 本編・番宣のグラフィック制作

### 5. Notion運用には独自ルールがある
- 制作管理DBのデータソースIDは `42c2f71c-c698-4ebb-9046-ebe137391bbb`
- チェックボックス系は boolean ではなく `__YES__` / `__NO__` の文字列で指定する
- ステータス値は `企画中 / 台本作成中 / 素材収録中 / 編集中 / 公開待ち / 公開済み` の固定6種のみ
- 動画番号は本編=整数、番宣=小数で紐付ける
- SQL的クエリは有料制限があるため、data_source_url指定検索を使う

### 6. Remotion構成にも一貫ルールがある
- シーンは Phase完全分離の Sequence コンポーネントで組む
- 尺は `timing.ts` に秒数で一元管理する
- VOICEVOX実尺に合わせて調整する前提で設計する

### 7. ブラウザ実行エージェントは仮説段階で扱う
- Antigravity を制作実行担当として使い、Google Vids の各シーンへナレーション本文を入力する構想が追加された。
- ただしこれは確認済み機能ではなく、シーン識別、本文改変防止、20〜30シーン安定処理、途中再開、再照合が要検証である。
- 運用に入れる前提条件は、「最後は人が確認する」工程を残したうえで、完成済み台本を安全に流し込めること。

## 制作フローへの示唆
- チャンネルの強みは、AIツールを雑に全部使うことではなく、用途別に使い分ける設計にある。
- 昭和AIでは「実用」と「安心感」が重要なので、生成物の正確性と確認工程を残す方が相性がよい。
- 企画・台本・サムネ・本編・保管までを別レイヤーで管理する発想がすでにある。

## 現時点で見えている未着手論点
- #13 / #15 のRemotion本編制作
- #15サムネの最終判断
- ブレスト案のDB登録
- Remotionプロジェクトzipの保管とNotionリンク化

## 関連
- [昭和AI チャンネルコンセプト](../showa-ai/昭和AI チャンネルコンセプト.md)
- [昭和世代に響くAI動画の特徴](../showa-ai/昭和世代に響くAI動画の特徴.md)
- [Antigravityによる昭和AI・Google Vidsナレーション制作自動化](../hermes/Antigravityによる昭和AI・Google Vidsナレーション制作自動化.md)
- [AI YouTubeトレンド（日米・2026-07）](../ai-research/AI YouTubeトレンド（日米・2026-07）.md)
- [2026-07-12_showa-ai-channel-concept-excerpt](../../sources/2026-07-12_showa-ai-channel-concept-excerpt.md)
- [2026-07-12_showa-ai-channel-handoff](../../sources/2026-07-12_showa-ai-channel-handoff.md)
- [2026-07-25_antigravity-google-vids-showa-ai-automation](../../sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md)

## 根拠 / 出典
- [2026-07-12_showa-ai-channel-concept-excerpt](../../sources/2026-07-12_showa-ai-channel-concept-excerpt.md)
- [2026-07-12_showa-ai-channel-handoff](../../sources/2026-07-12_showa-ai-channel-handoff.md)
- [2026-07-25_antigravity-google-vids-showa-ai-automation](../../sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md)

## 未解決
- Notion内の「7章の知見」の具体内容未取得
- 実際の制作進捗はNotion正本との差分確認が必要
- ブレスト18本の登録やRemotion保管など、制作管理タスクとWiki知識の橋渡し方法の整理
