PYTHON ?= python3
VENV ?= .venv
ACTIVATE = . $(VENV)/bin/activate

.PHONY: install
install:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && pip install -e ".[dev]"

.PHONY: test
test:
	$(ACTIVATE) && pytest

.PHONY: run
run:
	$(ACTIVATE) && flask --app app.main run --port 8000
