install:
		poetry install

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

selfcheck:
		poetry check

test:
		poetry run pytest

lint:
		poetry run flake8 gendiff

check: selfcheck test lint

build: check
		poetry build

.PHONY: install publish selfcheck test lint check build
