---
type: topic
title: "Antigravityによる昭和AI・Google Vidsナレーション制作自動化"
description: "昭和AIの完成済みナレーション台本をシーン単位に分割し、Antigravity を制作実行エージェントとして使って Google Vids の各シーンへ対応するナレーション/スクリプトを入力する制作自動化の仮説。"
status: active
created: 2026-07-25
updated: 2026-07-25
tags:
  - topic
  - karpathywiki
source: karpathywiki
legacy_path: "02_Topics/Antigravityによる昭和AI・Google Vidsナレーション制作自動化.md"
---

# Antigravityによる昭和AI・Google Vidsナレーション制作自動化

## 定義
昭和AIの完成済みナレーション台本をシーン単位に分割し、Antigravity を制作実行エージェントとして使って Google Vids の各シーンへ対応するナレーション/スクリプトを入力する制作自動化の仮説。

## 確認済み事項
- 現時点で Wiki に取り込まれた内容は、完成済み機能ではなく「仮説・検証予定」である。
- 構想上の役割分担は、ChatGPT = 発想・相談・意思決定、Hermes / KANBAN = 長期管理・自動処理、KarpathyWiki = 長期記憶、Antigravity = 実制作の実行、Google Vids = 映像・ナレーション制作先、である。
- 想定フローには、企画→リサーチ→台本作成→シーン分割→Antigravity→Google Vids→各シーンへのナレーション入力→入力照合→Vids 側ナレーション生成、が含まれている。

## この構想で大事なこと
- SDLC 的な「役割分担されたエージェント運用」を、ソフトウェア開発ではなく動画制作へ移植している点が重要。
- Antigravity はアイデア出し役ではなく、制作の実行担当/司令塔として想定されている。
- Hermes KANBAN と KarpathyWiki を組み合わせることで、単発自動化ではなく、継続運用しながら改善履歴を残す前提になっている。
- 昭和AI文脈では「最後は人が確認する」という安心設計を残すことが重要で、完全無人化よりも確認点の設計が価値になる。

## 想定フロー
1. ChatGPT や人間側で企画・相談・意思決定を行う。
2. Hermes / KANBAN でリサーチ、長期タスク管理、継続処理を回す。
3. 完成済みナレーション台本をシーン単位に分割し、シーン番号と本文の対応表を作る。
4. Antigravity が Google Vids をブラウザ操作し、各シーンのナレーション/スクリプト欄へ対応する本文を入力する。
5. 入力後、シーン番号と本文の対応を再照合する。
6. 必要に応じて Google Vids 側のナレーション生成へ進む。
7. 人間が最終確認し、公開前の品質を担保する。

## 仮説・アイデア
- 昭和AIの制作では、完成済み台本の「流し込み」と「照合」を自動化できると、制作負荷の大きい中間工程を短縮できる可能性がある。
- シーン別台本の対応表を明示的に持てば、途中失敗時の再開制御も設計しやすくなる可能性がある。
- この運用は、将来的に Google Vids 以外のブラウザ型制作ツールへも横展開できるかもしれない。

## 未確認 / 要検証
1. Antigravity が Google Vids を安定してブラウザ操作できるか。
2. シーン番号とナレーション台本を正しく対応付けられるか。
3. 台本本文を勝手に変更せず入力できるか。
4. 20〜30 シーン程度でも安定して処理できるか。
5. 途中で失敗した場合に、完了済みシーンを認識して途中から再開できるか。
6. 全入力後にシーンと台本の対応を再チェックできるか。
7. Vids 側のナレーション生成までどこまで自動化できるか。
8. 人間の最終確認をどこに残すべきか。

## 運用上の含意
- これは「AIが全部作る」話ではなく、完成済み台本を安全に実装する制作実行の自動化として整理した方がよい。
- 昭和AIの既存方針である「用途別にツールを分ける」「正確性が必要な箇所は確認工程を残す」と整合する。
- うまく行けば、KarpathyWiki には企画知識だけでなく、制作自動化の再利用パターンも蓄積できる。

## 関連
- [昭和AI チャンネル運用ルール](../antigravity/昭和AI チャンネル運用ルール.md)
- [昭和AI チャンネルコンセプト](../showa-ai/昭和AI チャンネルコンセプト.md)
- [昭和世代に響くAI動画の特徴](../showa-ai/昭和世代に響くAI動画の特徴.md)
- [GitHub Issue経由のKarpathyWiki取り込み](GitHub Issue経由のKarpathyWiki取り込み.md)
- [AI YouTubeトレンド（グローバル・2026-07）](../ai-research/AI YouTubeトレンド（グローバル・2026-07）.md)
- [2026-07-25_antigravity-google-vids-showa-ai-automation](../../sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md)

## 根拠 / 出典
- [2026-07-25_antigravity-google-vids-showa-ai-automation](../../sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md)
- https://github.com/hotaruyu/hermes-agent/issues/3
