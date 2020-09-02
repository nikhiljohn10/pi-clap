PROJECT     := pi-clap
AUTHOR      := Nikhil John
SRCDIR      := ./piclap
DOCSDIR     := ./docs
DOCSRCDIR   := $(DOCSDIR)/source
DOMAIN      := $(PROJECT).nikz.in
DOCTHEME    := sphinx_rtd_theme
RELEASE     := $(shell cat $(SRCDIR)/__init__.py | grep __version__ | sed -e 's/^.* = '\''//' -e 's/'\''//')
VERSION     := $(shell echo $(RELEASE) | sed -e 's/^\([0-9]*\.[0-9]*\).*$$/\1/')

help: version
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  version        to display package version"
	@echo "  setup          to install development dependencies"
	@echo "  remove         to remove development dependencies"
	@echo "  run            to run example app"
	@echo "  clean          to clean the build and execution temp files and directories"
	@echo "  build          to build PyPi package"
	@echo "  publish        to upload python package to PyPi server"
	@echo "  test-publish   to upload python package to TestPyPi server"
	@echo "  install        to install python package from PyPi server"
	@echo "  test-install   to install python package from TestPyPi server"
	@echo "  docs-clean     to clean the documentation directory"
	@echo "  docs-build     to make documentation source directory"
	@echo "  docs-html      to make standalone HTML documentation files for Github Pages"

version:
	@echo "\n\t#################################"
	@echo "\t#\t\t\t\t#"
	@echo "\t#\t $(PROJECT)  v$(RELEASE)\t#"
	@echo "\t#\t\t\t\t#"
	@echo "\t#################################\n"

setup:
	@python3 -m pip install -Ur requirements.txt

remove:
	@python3 -m pip uninstall -yr requirements.txt

test: setup
	@pytest

run: setup
	@python3 ./example/advanced.app.py

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean: clean-build
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '.DS_Store' -exec rm -f {} +
	@find . -name 'Thumbs.db' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '.pytest_cache' -exec rm -rf {} +

build: clean test
	@python3 setup.py sdist bdist_wheel

publish: build
	@twine upload dist/*
	@make clean

test-publish: build
	@twine upload --repository testpypi dist/*
	@make clean

install: clean setup
	@python3 -m pip install pi-clap==$(RELEASE)

test-install: clean setup
	@python3 -m pip install --index-url https://test.pypi.org/simple/ pi-clap==$(RELEASE)

uninstall:
	@python3 -m pip uninstall pi-clap

docs-clean:
	@rm -rf $(DOCSDIR)/_* $(DOCSDIR)/*.* $(DOCSDIR)/.buildinfo $(DOCSRCDIR)/_build/*

docs-build: version
	@echo "Compiling package documentation"
	@sphinx-apidoc -f -F -e -a -l -d 5 -H '$(PROJECT)' -A '$(AUTHOR)' -V '$(VERSION)' -R '$(RELEASE)' -o $(DOCSRCDIR) $(SRCDIR)
	@sed -i '' -e 's/path\.insert\(.*\)$$/path.append\('\''..\/..'\''\)/' -e "s/alabaster/$(DOCTHEME)/" $(DOCSRCDIR)/conf.py

docs-html: docs-clean
	@cd $(DOCSRCDIR) && make html
	@echo 'Moving HTML files to docs directory'
	@cp -af $(DOCSRCDIR)/_build/html/. $(DOCSDIR)
	@echo 'Configuring docs for Github pages'
	@echo '$(DOMAIN)' > $(DOCSDIR)/CNAME
	@echo 'Documentation successfully created.'
	@touch $(DOCSDIR)/.nojekyll

.PHONY:
	help
	test
	version
	setup
	clean
	build
	publish
	install
