.PHONY: build upload test check clean
	
install:
	python3 -m pip install .

dev-install:
	python3 -m pip install -e .[dev]

build:
	python3 -m build

upload: clean build
	twine upload dist/*

test:
	# Create rsks directory (if it doesn't exist)
	mkdir -p tests/rsks
	# Do a few steps in in the test/rsks directory:
	#  1. Initialize git repo if it hasn't been already,
	#  2. Add the rsk-files LFS git repo as remote origin,
	#  3. Set spare checkout to true. This will allow us to checkout specific files
	#     only, ignoring the rest.
	#  4. Add the "rsktools" directory as the only thing we actually care to checkout
	#  5. Pull in case any changes were made
	cd tests/rsks \
	; if [ ! -d .git ] ; then git init -q ; fi \
	; git remote add -f origin git@bitbucket.org:rbr/rsk-files.git 2>/dev/null \
	; git config core.sparseCheckout true \
	; echo "rsktools" > .git/info/sparse-checkout \
	; git pull origin master
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
