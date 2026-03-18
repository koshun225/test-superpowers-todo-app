# TODO App Design Spec

## Overview

Superpowersの使い方を学ぶためのチュートリアル用TODOアプリ。Zenn記事向けに、見栄えが良くかつシンプルな実装を目指す。

## Tech Stack

- **Backend**: Python FastAPI + SQLAlchemy + SQLite
- **Frontend**: HTMX + Jinja2 テンプレート (Node.js/npm不要)
- **Styling**: 素のCSS（フレームワーク不使用）
- **Design**: ミニマル・モノトーン（Notion風）

## Project Structure

```
├── main.py              # ルーティング・DB設定・アプリ全体
├── templates/
│   ├── base.html        # 共通レイアウト (HTMX CDN, style.css)
│   ├── index.html       # メインページ (入力フォーム + フィルター + リスト領域)
│   └── partials/
│       ├── todo_list.html   # タスクリスト全体 (ループ + 件数表示)
│       └── todo_item.html   # タスク1件 (チェック, タイトル, 削除)
├── static/
│   └── style.css        # 全スタイル定義
├── requirements.txt
└── tests/
    └── test_main.py     # APIテスト
```

シングルファイル構成。main.py 1ファイルにロジックを集約し、記事の読者がファイル間を行き来せずに全体像を把握できるようにする。

## Data Model

SQLiteテーブル1つ。SQLAlchemy ORMを使用。

```python
class Todo:
    id: int              # 主キー、自動採番
    title: str           # タスク名
    completed: bool      # 完了フラグ (default: False)
    created_at: datetime # 作成日時 (ソート用)
```

## API Endpoints

HTMXに合わせ、JSONではなくHTMLパーシャルを返す。

| Method | Path | Action | Response |
|--------|------|--------|----------|
| GET | `/` | タスク一覧ページ表示 | `index.html`（全体ページ） |
| POST | `/todos` | タスク追加 | `todo_list.html`（リスト全体partial） |
| PUT | `/todos/{id}/toggle` | 完了トグル | `todo_item.html`（1件partial） |
| PUT | `/todos/{id}` | タイトル編集 | `todo_item.html`（1件partial） |
| DELETE | `/todos/{id}` | タスク削除 | `todo_list.html`（リスト全体partial） |
| GET | `/todos?filter=all\|active\|completed` | フィルター | `todo_list.html`（リスト全体partial） |

### HTMX Swap Strategy

- **完了トグル・編集**: 該当1件だけ差し替え (`hx-swap="outerHTML"`)
- **追加・削除・フィルター**: リスト全体を差し替え（件数表示も更新するため）

## Template & HTMX Flow

### テンプレート構成

- **`base.html`**: 共通レイアウト。HTMX CDN読み込み、style.css読み込み
- **`index.html`**: メインページ。入力フォーム + フィルターボタン + `#todo-list` 領域
- **`partials/todo_list.html`**: タスクリスト全体。todo_item.htmlをループ呼び出し + 件数表示
- **`partials/todo_item.html`**: タスク1件。チェックボックス、タイトル（ダブルクリックで編集）、削除ボタン

### 操作フロー

```
[タスク追加]
  入力欄に入力 → Enter
  → POST /todos (hx-post)
  → #todo-list 内を todo_list.html で差し替え
  → 入力欄クリア

[完了トグル]
  チェックボックスクリック
  → PUT /todos/{id}/toggle (hx-put)
  → その1件を todo_item.html で outerHTML 差し替え（打ち消し線付与）

[インライン編集]
  タイトルをダブルクリック → input表示
  → Enter で PUT /todos/{id} (hx-put)
  → 編集後の todo_item.html で差し替え

[削除]
  削除ボタンクリック
  → DELETE /todos/{id} (hx-delete)
  → #todo-list 内を todo_list.html で差し替え

[フィルター]
  フィルターボタンクリック
  → GET /todos?filter=active (hx-get)
  → #todo-list 内を todo_list.html で差し替え
```

## Styling

CSS は `static/style.css` 1ファイル。フレームワーク不使用。

### Design Tokens

- **Font**: `system-ui, -apple-system, sans-serif`
- **Colors**: `#fff` / `#111` / `#666` / `#e5e5e5` / `#fafafa` / `#999`
- **Container**: max-width `600px`, center-aligned
- **Border**: `1px solid #e5e5e5`, border-radius `4px`
- **Active filter**: `border-bottom: 2px solid #111`
- **Completed task**: `text-decoration: line-through`, color `#999`
- **Hover**: background `#fafafa`
- **Transition**: `background 0.15s ease`

モバイル対応はスコープ外。

## Dependencies

### requirements.txt

```
fastapi
uvicorn
sqlalchemy
jinja2
```

### Dev Dependencies

```
pytest
httpx
```

## Running

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Testing

- `pytest` + `httpx` の `AsyncClient` でAPIテスト
- テスト用DBは `:memory:` SQLite を使用
- テンプレートレスポンスのステータスコードとHTML内容を検証
