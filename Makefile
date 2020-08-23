project_name = pi-clap
.PHONY:
	setup
	test
	clean-build
	clean
	build
	publish
	test-publish
	docs
	run

setup:
	pip3 install -Ur requirements.txt

test: setup
	python3 ./tests/test_settings.py

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean: clean-build
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

build: clean test
	pip3 install twine
	python3 setup.py sdist bdist_wheel

publish: build
	twine upload dist/*

test-publish: build
	twine upload --repository testpypi dist/*

docs:
	sphinx-apidoc -f -F -e -M -a -H 'pi-clap' -A 'Nikhil John' -V '1.1.x' -R '1.1' -o ./sphinx ./piclap

run: setup
	python3 ./example/app.py
