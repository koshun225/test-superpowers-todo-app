# TODO App

FastAPI + HTMX + SQLite で作ったシンプルなTODOアプリ。

Claude Code + [Superpowers](https://github.com/anthropics/claude-code-plugins) を使って、プロンプトひとつから設計・実装しました。

![TODOアプリ](docs/screenshots/作業中.png)

## 機能

- タスクの追加・編集・削除
- 完了/未完了のトグル
- フィルター（All / Active / Completed）
- インライン編集（ダブルクリック）

## 技術スタック

- **Backend**: Python FastAPI + SQLAlchemy + SQLite
- **Frontend**: HTMX + Jinja2
- **Styling**: Vanilla CSS（ミニマル・モノトーン）

## セットアップ

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

http://localhost:8000 で起動します。

## テスト

```bash
pytest tests/test_main.py -v
```
