PYTHON ?= python3
API_DIR := api

.PHONY: help api-install api-run api-test install run test git-flow-init git-flow-feature-start git-flow-release-start git-flow-hotfix-start

help:
	@echo "Targets available:"
	@echo "  make install     - Install API dependencies"
	@echo "  make run         - Run FastAPI app"
	@echo "  make test        - Run API tests"
	@echo "  make git-flow-init               - Initialize Git Flow defaults"
	@echo "  make git-flow-feature-start NAME=feature-name"
	@echo "  make git-flow-release-start NAME=0.1.0"
	@echo "  make git-flow-hotfix-start NAME=0.1.1"

api-install:
	cd $(API_DIR) && $(PYTHON) -m pip install -r requirements-dev.txt

api-run:
	cd $(API_DIR) && $(PYTHON) -m app.run

api-test:
	cd $(API_DIR) && pytest -q

install: api-install

run: api-run

test: api-test

git-flow-init:
	@command -v git-flow >/dev/null 2>&1 || (echo "git-flow not found. Install first (macOS: brew install git-flow-avh)" && exit 1)
	git flow init -d

git-flow-feature-start:
	@test -n "$(NAME)" || (echo "Use NAME=<feature-name>" && exit 1)
	git flow feature start $(NAME)

git-flow-release-start:
	@test -n "$(NAME)" || (echo "Use NAME=<version>" && exit 1)
	git flow release start $(NAME)

git-flow-hotfix-start:
	@test -n "$(NAME)" || (echo "Use NAME=<version>" && exit 1)
	git flow hotfix start $(NAME)