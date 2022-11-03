.PHONY: build upload test check clean
	
install:
	python3 -m pip install .

dev-install:
	python3 -m pip install -e .'[dev]'

build:
	python3 -m build

upload: clean build
	twine upload dist/*

test:
	# Run tests
	python3 -m unittest discover tests

format-check: 
	black --check pyrsktools

type-check:
	mypy --config mypy.ini pyrsktools

check: type-check format-check
	
clean:
	# Clean up build artifacts.
	-rm -R build dist pyRSKtools.egg-info
	# Clean up bytecode leftovers.
	find . -type f -name '*.pyc' -print0 | xargs -0 rm
	find . -type d -name '__pycache__' -print0 | xargs -0 rmdir
