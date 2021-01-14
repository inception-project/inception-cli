test:
	python -m pytest tests/

black:
	black -l 120 inception/
	black -l 120 tests/

html:
	cd docs && make html