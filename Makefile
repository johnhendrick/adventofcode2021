all: clean testing build upload clean

testing:
	pytest test

build-dev:
	python -m pip install -e .

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info
