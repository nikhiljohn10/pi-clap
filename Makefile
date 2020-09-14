PROJECT     := pi-clap
AUTHOR      := Nikhil John
SRCDIR      := ./piclap
DOCSDIR     := ./docs
DOCSRCDIR   := $(DOCSDIR)/source
DOMAIN      := $(PROJECT).nikz.in
DOCTHEME    := sphinx_rtd_theme
RELEASE     := $(shell cat $(SRCDIR)/__init__.py | grep __version__ | sed -e 's/^.* = '\''//' -e 's/'\''//')
VERSION     := $(shell echo $(RELEASE) | sed -e 's/^\([0-9]*\.[0-9]*\).*$$/\1/')

PY_VER      := $(shell python3 -V | sed -e 's/^Python //')
PYAUDIO     := 0.2.11

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
	@echo "  local-install  to install python package from local build"
	@echo "  docs-clean     to clean the documentation directory"
	@echo "  docs-build     to make documentation source directory"
	@echo "  docs-html      to make standalone HTML documentation files for Github Pages"

version:
	@echo "\n\t#################################"
	@echo "\t#\t\t\t\t#"
	@echo "\t#\t $(PROJECT)  v$(RELEASE)\t#"
	@echo "\t#\t\t\t\t#"
	@echo "\t#################################\n"

setup: remove
ifeq (Darwin,$(findstring Darwin, $(shell uname)))
	@if ! [[ $(PY_VER) =~ ^3\.[6-8]\.[0-9]+.*$$ ]]; then /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python3 ; fi;
endif
	@python3 -m pip install --user -U setuptools wheel
ifeq (Darwin,$(findstring Darwin, $(shell uname)))
	@python3 -m pip install --user pyaudio==$(PYAUDIO) || python3 -m pip install --user --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio==$(PYAUDIO)
endif
	@python3 -m pip install --user -Ur requirements.txt

remove:
	@python3 -m pip uninstall -yr requirements.txt

test:
	@pytest

run:
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
	@twine check dist/*

publish: build
	@twine upload dist/*
	@make clean

test-publish: build
	@twine upload --repository testpypi dist/*
	@make clean

install: clean setup
	@python3 -m pip install --user pi-clap==$(RELEASE)

test-install: clean setup
	@python3 -m pip install --user --index-url https://test.pypi.org/simple/ pi-clap==$(RELEASE)

local-install: build
	@python3 -m pip install --user dist/pi_clap-$(RELEASE)-py3-none-any.whl

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
	remove
	clean
	build
	publish
	install
