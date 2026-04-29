.PHONY: install build serve update check

install:
	uv sync --group dev

build:
	uv run python -m exocortex
	zola build

serve:
	zola serve

update:
	uv lock --upgrade

check:
	uv run ruff format --check .
	uv audit
	uv run ruff check --select I .
	uv run ruff check .
	uv run ty check exocortex/
