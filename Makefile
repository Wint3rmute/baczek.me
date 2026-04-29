.PHONY: install build serve update

install:
	uv sync --group dev

build:
	uv run python -m exocortex
	zola build

serve:
	zola serve

update:
	uv lock --upgrade
