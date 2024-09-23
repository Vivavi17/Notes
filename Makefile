app_port = 8080
export PYTHONPATH = $(shell echo $PYTHONPATH):$(shell pwd)

start:
	docker compose up --build

run_app:
	python3 src/main.py

test:
	pytest -s

venv:
ifeq (,$(wildcard venv))
	@echo "Creating venv"
	python3 -m venv venv
	@echo "For activate venv and install requirements:"
	@echo "source venv/bin/activate && pip install -r requirements.txt"
endif

env_file:
ifeq (,$(wildcard .env))
	@echo "Creating .env file from .env-example..."
	cp .env-example .env
endif

clean_volumes:
	docker volume ls -q | xargs docker volume rm