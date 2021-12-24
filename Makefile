install:
		poetry install

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

test-coverage:
		poetry run pytest --cov=gendiff tests --cov-report xml

selfcheck:
		poetry check

test:
		poetry run pytest

lint:
		poetry run flake8 gendiff

check: selfcheck lint test

build: check
		poetry build

.PHONY: install publish selfcheck test lint check build
