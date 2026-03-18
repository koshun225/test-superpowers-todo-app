---
title: "Claude Codeに\"Superpowers\"を入れたら、プロンプト1行からTODOアプリが完成した"
emoji: "⚡"
type: "tech"
topics: ["claudecode", "superpowers", "ai", "python"]
published: false
---

## プロンプトひとつで、ここまでできた

最初に投げたプロンプトは、これだけです。

```
TODOアプリを作りたい。superpowersの使い方を学ぶチュートリアル的に作ってみたい。
その内容をZennの記事にしたいから、そこそこ見栄えがいいやつで。
ただし実装はシンプルに。pythonのfastapiを使って。フロントエンドはお任せで。
```

そして、できあがったのがこちら。

![完成したTODOアプリ](/images/作業中.png)

FastAPI + HTMX + SQLiteで動くTODOアプリ。タスクの追加・完了・編集・削除・フィルターまでついて、デザインもNotion風のミニマルな仕上がりです。

このアプリは、上のプロンプトから始まって、Claudeの質問に答えていくだけで完成しました。コードを1行も自分で書いていません。でも、技術選定もデザインの方向性も、すべて自分で決めた実感があります。

その体験を支えていたのが **Superpowers** というClaude Codeのプラグインでした。

## Superpowersとは

Superpowersは、Claude Codeに「設計フェーズ」を追加するプラグインです。インストールは1行で終わります。

```
claude install-plugin superpowers
```

導入すると、`brainstorm` → `plan` → 実装 → `code-review` という一連のワークフローが使えるようになります。brainstormで要件を対話的に固め、planで実装手順を整理し、コードを書いたらcode-reviewで品質をチェックする——という流れです。

ポイントは、「AIに丸投げしてコードを出してもらう」のではなく、「AIと対話しながら設計し、自分で判断して進める」ということ。この違いが、できあがったものへの納得感を大きく変えてくれます。
