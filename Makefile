init-dev:
	pip install -r dev.txt

test:
	pip install -e .
	py.test
