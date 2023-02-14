.DEFAULT_GOAL := help

## WEB:
server.install:                     ## Install server
	docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

server.start:                       ## Start server
	docker-compose up server

server.bash:                        ## Bash to server
	docker-compose exec server bash

server.daemon:                      ## Start server as daemon
	docker-compose up -d server

server.stop:                        ## Stop server
	docker-compose stop server

server.logs:                        ## Display server logs
	tail -f server.log

server.upgrade:                     ## Upgrade server
	docker-compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"

## CLI:
cli.install:                        ## Install requirements for cli
	docker-compose run --rm cli pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

cli.start:                          ## Start & bash to CLI container
	docker-compose up -d cli
	docker-compose exec cli bash

cli.stop:                           ## Stop cli container
	docker-compose stop cli

## TEST:
test: test.run
test.run:                           ## Run all test cases on test-server
	python -m pytest visionai/ -W ignore

test.coverage:                      ## Generate test coverage
	coverage run -m pytest --cov-report html:coverage

lint: test.lint
test.lint:                          ## Lint test
	python -m flake8  ./visionai

safety: test.safety
test.safety:                        ## Safety check
	python -m safety check

## PACKAGE:
package.build:                      ## Build package
	docker-compose build packageserver

package.test:                       ## Test package
	docker-compose run --rm packageserver bash -c "python -m pytest"

## FORMAT:
format.black:                       ## Run black on every file (DON'T USE)
	docker-compose run --rm server bash -c "python vendor/bin/black models/ routes/ test/ util/ *.py --exclude vendor/ --skip-string-normalization"

format.isort:                       ## Sort imports for every file (CAN USE)
	docker-compose run --rm server bash -c "python vendor/bin/isort -rc models/ routes/ test/ util/ *.py --skip vendor/"

## HELP:
.PHONY: help
help:                               ## Display help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//'
