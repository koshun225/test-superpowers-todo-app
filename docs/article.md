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
