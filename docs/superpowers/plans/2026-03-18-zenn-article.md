# Zenn記事 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Claude Code + Superpowersを使ったTODOアプリ開発体験のZenn記事を作成する

**Architecture:** Zenn CLIのMarkdown記事形式（frontmatter + 本文）で1ファイル作成。画像はdocs/screenshots/から参照。

**Tech Stack:** Zenn Markdown, 画像ファイル（PNG）

**Spec:** `docs/superpowers/specs/2026-03-18-zenn-article-design.md`

---

## File Structure

- Create: `docs/article.md` — Zenn記事本体（frontmatter + 全セクション）
- Reference: `docs/screenshots/image.png` — brainstormデザイン選択画面
- Reference: `docs/screenshots/作業中.png` — 完成したTODOアプリ

---

### Task 1: 記事ファイル作成 — frontmatter + セクション1（冒頭）

**Files:**
- Create: `docs/article.md`

- [ ] **Step 1: frontmatterとセクション1を書く**

Zenn frontmatterを含むファイルを作成。セクション1（フック）として:
- タイトル
- 投げたプロンプト（コードブロック）
- 完成品スクリーンショット（作業中.png）
- 引き込みの一文

```markdown
---
title: "Claude Codeに\"Superpowers\"を入れたら、プロンプト1行からTODOアプリが完成した"
emoji: "⚡"
type: "tech"
topics: ["claudecode", "superpowers", "ai", "python"]
published: false
---

（セクション1の本文）
```

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add Zenn article draft — section 1 (hook)"
```

---

### Task 2: セクション2 — Superpowersとは

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: セクション2を追記**

短めの導入（3〜5行）:
- Claude Codeの拡張プラグインであること
- brainstorm → plan → 実装 → code-reviewのワークフロー
- 「AIに丸投げ」ではなく「AIと対話しながら設計→実装」
- インストール方法（1行コマンド）

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 2 — what is Superpowers"
```

---

### Task 3: セクション3-1 — プロンプトと仕様書の比較

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: 比較表を追記**

プロンプトで言ったこと vs 仕様書で決まったことの表（6行: Backend, Frontend, デザイン, 構成, 機能, テスト）。表の後に「曖昧な指示が具体的な設計に変換された」ことを一文で。

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 3-1 — prompt vs spec comparison"
```

---

### Task 4: セクション3-2 — brainstormとの問答の流れ

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: 問答の流れを追記**

「おおよそこのような問答があった」と前置きした上で、5つの問答を紹介。ビジュアルコンパニオンのスクリーンショット（image.png）を挿入。

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 3-2 — brainstorm Q&A flow"
```

---

### Task 5: セクション3-3 — 質問の「質」と他サービスとの違い

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: 質問の質について追記**

- 他ツールとの比較（即コード生成 vs まず理解しようとする）
- 選択肢形式の具体例（フロントエンド選定の例を再現）
- おすすめ明示 + 影響範囲の説明
- 「自分で選んだ」納得感

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 3-3 — quality of brainstorm questions"
```

---

### Task 6: セクション4 — plan → 実装 → code-review

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: ワークフロー紹介を追記**

plan, 実装, code-reviewの3つを軽く紹介。「一貫したワークフローが自動的に回る」というまとめ。

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 4 — plan, implementation, code-review workflow"
```

---

### Task 7: セクション5 — 完成品とまとめ

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: まとめを追記**

- 完成品スクリーンショット再掲（作業中.png）
- イメージ通りの仕上がり
- Superpowersの本質（「AIと一緒に設計する」体験）
- 導入方法・参考リンク

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: add section 5 — conclusion and final result"
```

---

### Task 8: 全体通し読みと最終調整

**Files:**
- Modify: `docs/article.md`

- [ ] **Step 1: 全体を通し読みして調整**

- 文体の統一（です/ます調）
- セクション間の流れが自然か
- 画像参照が正しいか
- 5〜10分の読了時間に収まっているか（目安: 2000〜4000文字）
- 冗長な箇所を削る

- [ ] **Step 2: コミット**

```bash
git add docs/article.md
git commit -m "docs: finalize Zenn article draft"
```
