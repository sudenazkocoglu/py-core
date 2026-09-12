.PHONY: install test lint all

install:
	uv sync --dev

test:
	pytest

lint:
	mypy --strict src/

all: test lint
