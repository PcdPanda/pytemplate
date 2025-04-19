.PHONY : doc clean
PYTHON ?= python
PYTEST ?= pytest


all:

setup-dev:
	pip install -r requirements.txt

build: 
	python setup.py build_ext

clean:
	$(PYTHON) setup.py clean

doc:# Need pip install sphinx breathe piccolo-theme
	-rm -rf doc/build doc/source/generated
	cd doc; \
	$(MAKE) html

render-doc: doc
	python -m http.server --directory doc/build/html

dev: build
	python -m pip install --no-build-isolation -e .

test-cov:
	rm -rf coverage .coverage
	$(PYTEST)

test: test-cov

tidy:
	rm -rf build
	ruff format
	tidy-imports . -r --quiet

clean-cpp: 
	rm -rf src/python/cpp/lib
	rm -rf src/cpp/build

make-cpp:
	mkdir -p src/cpp/build
	cd src/cpp/build && cmake .. --debug-output
	
build-cpp: make-cpp
	cd src/cpp/build && cmake --build .

install-cpp: build-cpp
	cd src/cpp/build && make install

install-py: 
	pip install .

install-py-dev:
	pip install -e .

install-dev: install-cpp install-py-dev

install: install-cpp tidy install-py

lint:
	flake8