PYTHON_VERSION = 3.12
UV = uv
SRC = src
VENV = .venv
PY = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: check-uv check-django start-venv migrate entrypoint start-app freeze clean

check-uv:
	@command -v $(UV) >/dev/null 2>&1 || { \
		echo >&2 "✖ 'uv' не установлен. Установи через 'pip install uv' или см. https://github.com/astral-sh/uv"; \
		exit 1; \
	}

check-django:
	@$(PY) -c "import django" 2>/dev/null || { \
		echo >&2 "✖ Django не установлен в виртуальной среде. Запусти 'make start-venv' сначала."; \
		exit 1; \
	}

start-venv: check-uv
	uv sync

migrate: check-django
	@echo "▶ Миграции..."
	uv run python $(SRC)/manage.py makemigrations game player user
	uv run python $(SRC)/manage.py migrate
	@echo "✓ Миграции выполнены."

entrypoint: check-django
	@echo "▶ Запуск entrypoint..."
	uv run python $(SRC)/entrypoint.py

start-app: start-venv migrate entrypoint

freeze:
	@echo "▶ Сохраняем зависимости..."
	$(PY) -m pip freeze > requirements.txt
	@echo "✓ requirements.txt обновлён."

clean:
	@echo "⚠ Очистка проекта..."
	rm -rf $(VENV) __pycache__ */__pycache__ *.pyc *.pyo *.pyd *.log
	find . -name '*.sqlite3' -delete
	find $(SRC) -type d -name 'migrations' -exec rm -rf {} +
	@echo "✓ Проект очищен."
