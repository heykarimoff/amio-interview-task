# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export COMPOSE_PROJECT_NAME=maze
export DOCKER_BUILDKIT=1

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs --tail=100

check-black:
	black --line-length 80 --diff --check .

check-isort:
	isort . --check --diff

check-flake8:
	flake8 $(find * -name '*.py') --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 $(find * -name '*.py') --count --exit-zero --max-complexity=10 --max-line-length=80 --statistics
