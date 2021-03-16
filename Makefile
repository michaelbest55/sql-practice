develop-local:
	docker-compose -p sql_practice-$(shell whoami) -f docker-compose.yml up --build

clean-local:
	docker-compose -p sql_practice-$(shell whoami) -f docker-compose.yml rm -s -v -f

.PHONY: all test clean
