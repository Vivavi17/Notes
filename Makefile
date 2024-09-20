app_port = 8080
export PYTHONPATH = $(shell echo $PYTHONPATH):$(shell pwd)

start:
	docker compose build
	docker compose up

run_app:
	python3 src/main.py
env_file:
ifeq (,$(wildcard .env))
	@echo "Creating .env file from .env-example..."
	cp .env-example .env
endif

clean_volumes:
	docker volume ls -q | xargs docker volume rm