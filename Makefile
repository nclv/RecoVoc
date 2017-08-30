TEST_PATH=tests/

init:
    python3 -m pip install -r requirements.txt

clean: clean-build
		rm -fr htmlcov/

clean-build:
		rm -fr build/
		rm -fr dist/
		rm -fr *.egg-info
		rm -fr .coverage
		rm -fr .cache

coverage:
		coverage run --source=recovoc setup.py test
		coverage report -m
		coverage html
		open htmlcov/index.html

test:
    python3 setup.py test

install: clean ## install the package to the active Python's site-packages
		python3 setup.py install

.PHONY: clean-build docs clean

help:
		@echo "clean-build - remove build artifacts"
		@echo "test - run tests quickly with the default Python3"
		@echo "coverage - check code coverage quickly with the default Python3"
		@echo "docs - generate Sphinx HTML documentation, including API docs"
