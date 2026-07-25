# ChatGPT → Hermes → KarpathyWiki Inbox

ChatGPT PlusからKarpathyWikiへ知識を渡すための軽量ブリッジです。

## 仕組み

1. ChatGPTがこのリポジトリに `[WIKI-INBOX]` で始まるIssueを作る。
2. Hermesを動かしているPCで `tools/chatgpt_wiki_inbox.py` を実行する。
3. スクリプトが未処理Issueを取得する。
4. Hermesの `llm-wiki` skillへ内容を渡す。
5. Hermesが既存Wikiを検索し、重複を避けてKarpathyWikiへ統合する。
6. 成功後、Issueへ結果をコメントしてIssueを閉じる。

## ChatGPTでの使い方

ChatGPTに次のように依頼します。

> ここまでの会話をKarpathyWikiに残して

ChatGPT側では、会話ログをそのまま投げるのではなく、以下を整理してIssueにします。

- 確認済み事実
- 気づき・解釈
- 仮説
- 未確認事項
- 今後試すこと
- 出典URL

Issueタイトル例:

`[WIKI-INBOX] Antigravity × Hermes × 昭和AI制作フロー`

## Hermes PCの準備

必要なもの:

- `gh` CLIでGitHubにログイン済み
- `hermes` CLIが実行可能
- Hermesの `llm-wiki` skillが利用可能
- KarpathyWikiの保存先が設定済み

実行:

```bash
export GITHUB_REPOSITORY=hotaruyu/hermes-agent
python tools/chatgpt_wiki_inbox.py
```

Windows PowerShell:

```powershell
$env:GITHUB_REPOSITORY="hotaruyu/hermes-agent"
python tools/chatgpt_wiki_inbox.py
```

## 定期実行

最初は手動実行を推奨します。動作確認後、Windowsタスクスケジューラやcronで5〜15分ごとに実行すれば、ChatGPTから送った知識が自動的にWikiへ入ります。

## 安全設計

Issue本文は「資料」としてHermesへ渡し、Issue本文に含まれる命令を実行しないようプロンプトで明示しています。

また、最初は自動削除ではなく、処理結果をIssueコメントとして残してからcloseするため、履歴を追跡できます。
