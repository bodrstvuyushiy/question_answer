manage = poetry run python src/manage.py

deps:
	poetry install --no-root

dev:
	docker compose up --build --detach
	make for_dev

run:
	$(manage) migrate
	$(manage) runserver

logs:
	docker compose logs -f

for_dev: fmt check test
	
up:
	docker compose up -d

down:
	docker compose down && docker network prune --force

fmt:
	poetry run mypy src
	poetry run ruff format
	poetry run ruff check --fix --unsafe-fixes
	poetry run toml-sort pyproject.toml
	make fmt-gitignore

fmt-gitignore:
	sort --output .gitignore .gitignore
	awk "NF" .gitignore > .gitignore.temp && mv .gitignore.temp .gitignore

check:
	$(manage) makemigrations --check --dry-run --no-input
	$(manage) check
	poetry run ruff format --check
	poetry run ruff check --unsafe-fixes
	poetry run flake8 tests --select AAA
	poetry run toml-sort pyproject.toml --check

test:
	poetry run pytest --create-db



