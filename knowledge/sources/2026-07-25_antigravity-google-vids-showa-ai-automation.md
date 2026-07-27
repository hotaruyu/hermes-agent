---
type: source
title: "2026-07-25 Antigravityによる昭和AI・Google Vidsナレーション制作自動化"
description: "Migrated from legacy KarpathyWiki: 04_Sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md"
status: active
created: 2026-07-25
updated: 2026-07-25
tags:
  - source
  - karpathywiki
source: karpathywiki
legacy_path: "04_Sources/2026-07-25_antigravity-google-vids-showa-ai-automation.md"
---

# 2026-07-25 Antigravityによる昭和AI・Google Vidsナレーション制作自動化

## Source
- Title: Antigravityによる昭和AI・Google Vidsナレーション制作自動化
- Origin: pasted source material supplied in chat for wiki ingestion
- Repository: https://github.com/hotaruyu/hermes-agent
- GitHub Issue provenance: https://github.com/hotaruyu/hermes-agent/issues/3
- Date added: 2026-07-25
- Scope: 昭和AIの完成済みナレーション台本をシーン単位に分割し、Antigravity を制作実行エージェントとして使って Google Vids の各シーンへ入力する自動化構想
- Note: このページは Issue 本文の実行ではなく、今回提示された source material を要約・構造化した provenance ページ。

## 確認済み事実
- 取り込み対象として提示された構想は、昭和AIの動画制作工程を Antigravity 中心に自動化するアイデアである。
- 想定フローには、企画、リサーチ、台本作成、シーン分割、Antigravity、Google Vids、シーンごとのナレーション入力、入力照合、Vids 側ナレーション生成が含まれている。
- source material では、Hermes KANBAN は長期タスク管理・継続処理、KarpathyWiki は長期知識基盤、Antigravity は制作実行、Google Vids は映像・ナレーション制作先として位置づけられている。
- source material 自体が、これは完成機能ではなく「仮説・検証予定」であると明示している。

## 気づき・解釈
- この構想の本質は、単なる台本貼り付け自動化ではなく、企画から制作実行までを役割分担した複数エージェント/複数基盤でつなぐ制作パイプライン設計にある。
- 昭和AI文脈では、視聴者向け動画の知識と、制作現場側の自動化知識が同じ Wiki に共存し始めている。
- 既存の昭和AI運用ルールにある「用途ごとにツールを分ける」「最後は人が確認する」と相性がよい構想である。

## 仮説
- Antigravity が Google Vids のシーン UI を安定識別できれば、完成済み台本のシーン別流し込み工程は省力化できる可能性がある。
- 人間が最終確認点を保持しつつ、Antigravity を制作実行担当、Hermes / KANBAN を長期管理担当として分けると、運用上の責任範囲が明確になる可能性がある。
- 20〜30 シーン規模の再開制御や照合工程まで扱えれば、昭和AIの標準制作パイプライン候補になりうる。

## 未確認事項
- Antigravity が Google Vids を安定してブラウザ操作できるか。
- シーン番号とナレーション台本を誤対応なく扱えるか。
- 台本本文を勝手に変えずに入力できるか。
- 20〜30 シーンでも失敗率や処理時間が実用範囲に収まるか。
- 途中失敗時に完了済みシーンを認識して途中再開できるか。
- 全入力後にシーンと台本の対応を再チェックできるか。
- Google Vids 側のナレーション生成まで、どこまで自動化できるか。
- 人間の最終確認をどの工程に残すべきか。

## 今後試すこと
- Google Vids の 1 本の短いダミー台本で、5 シーン前後の最小実験を行う。
- シーン識別、入力、再照合、失敗時再開の4点を最小成功条件として切り分けて試す。
- 成功/失敗ログを KarpathyWiki に反映し、仮説から運用知識へ昇格できるかを確認する。

## 反映先
- [Antigravityによる昭和AI・Google Vidsナレーション制作自動化](../topics/hermes/Antigravityによる昭和AI・Google Vidsナレーション制作自動化.md)
- [昭和AI チャンネル運用ルール](../topics/antigravity/昭和AI チャンネル運用ルール.md)
- [昭和AI チャンネルコンセプト](../topics/showa-ai/昭和AI チャンネルコンセプト.md)
- [昭和世代に響くAI動画の特徴](../topics/showa-ai/昭和世代に響くAI動画の特徴.md)
- [GitHub Issue経由のKarpathyWiki取り込み](../topics/hermes/GitHub Issue経由のKarpathyWiki取り込み.md)

## 次に考えること
- シーン分割の正本をどこに置くか。完成台本、シーン別JSON、Google Vids 側入力欄のどれを正本とみなすか。
- Antigravity と Hermes / KANBAN の責任分界を、制作実行・監視・記録の3層でどう固定するか。
- 実機検証の結果を受けて、このテーマを「制作ツール別の役割設計」や「人間の最終確認設計」へ抽象化できるか。
