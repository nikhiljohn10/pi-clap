project_name = pi-clap
.PHONY:
	setup
	test
	clean-pyc
	clean-build
	build
	publish
	test-publish
	run

setup:
	pip3 install -Ur requirements.txt

test: setup
	python3 ./tests/test_settings.py

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

clean-build: clean-pyc
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

build: clean-build test
	pip3 install twine
	python3 setup.py sdist bdist_wheel

publish: build
	twine upload dist/*

test-publish: build
	twine upload --repository testpypi dist/*

run: setup
	python3 ./tests/app.py
