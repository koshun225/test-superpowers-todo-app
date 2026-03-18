# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Tutorial TODO app built with FastAPI + HTMX + SQLite. Designed for a Zenn article about Superpowers.

## Commands

- **Run**: `uvicorn main:app --reload` (http://localhost:8000)
- **Test**: `pytest tests/test_main.py -v`
- **Install**: `pip install -r requirements.txt`

## Architecture

Single-file backend (`main.py`) with Jinja2 templates and HTMX.

- `main.py` — SQLAlchemy model, DB setup, all FastAPI routes. Returns HTML partials (not JSON) for HTMX.
- `templates/partials/` — HTMX swap targets. `todo_list.html` for list-level ops (add/delete/filter), `todo_item.html` for item-level ops (toggle/edit).
- `static/style.css` — Vanilla CSS, minimal monotone design. No framework.
- Tests use `FastAPI.TestClient` with in-memory SQLite via dependency override.
