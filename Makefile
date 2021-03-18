develop-local:
	docker-compose -p sql_practice-$(shell whoami) -f docker-compose.yml up --build

clean-local:
	docker-compose -p sql_practice-$(shell whoami) -f docker-compose.yml rm -s -v -f

migration_file:
	docker exec --user $(shell id -u):$(shell id -g) sql_practice-$(shell whoami)_python_db_1 \
	alembic revision --autogenerate -m $(MIGRATION_TITLE)

.PHONY: all test clean
