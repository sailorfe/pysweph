# pysweph Makefile

PYTHON := python3

.DEFAULT_GOAL := void

.PHONY: build clean install install-dev sdist dist test docs clean-docs live void

# -*- build & install

build:
	uv run $(PYTHON) setup.py build

install:
	uv run $(PYTHON) setup.py install

install-dev:
	uv run $(PYTHON) -m pip install -e .

sdist:
	uv run $(PYTHON) setup.py sdist --formats=gztar,xztar,zip

dist: sdist
	@echo "Source distributions created in dist/"

clean:
	rm -rf MANIFEST build dist .eggs *.egg-info *.so docs/_build/*

# -*- testing

test:
	PYTHONPATH=src uv run python -m unittest discover -s tests

# -*- documentation

BUILD_DIR := docs/_build
SPHINX_SOURCE_DIR := docs/
SPHINX_REQS := docs/requirements.txt

docs: clean-docs
	@echo "Building pysweph documentation..."
	uv run sphinx-build -b html $(SPHINX_SOURCE_DIR) $(BUILD_DIR)

clean-docs:
	@echo "Cleaning up documentation build directory ($(BUILD_DIR))..."
	rm -rf $(BUILD_DIR)

live: clean-docs
	@echo "Starting live documentation server for pysweph..."
	uv run --with-requirements $(SPHINX_REQS) sphinx-autobuild --host 0.0.0.0 $(SPHINX_SOURCE_DIR) $(BUILD_DIR) --watch $(SPHINX_SOURCE_DIR)

# -*- empty default target

void: ;
