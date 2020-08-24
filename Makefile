SRCDIR				:= ./piclap
DOCSDIR				:= ./docs
DOCSRCDIR			:= $(DOCSDIR)/source
PROJECT				:= $(shell cat $(SRCDIR)/__init__.py | grep __project__ | sed -e 's/^.* = '\"'//' -e 's/'\"'//')
AUTHOR				:= $(shell cat $(SRCDIR)/__init__.py | grep __author__ | sed -e 's/^.* = '\"'//' -e 's/'\"'//')
VERSION				:= $(shell cat $(SRCDIR)/__init__.py | grep __version__ | sed -e 's/^.* = '\"'//' -e 's/'\"'//')
RELEASE				:= $(shell cat $(SRCDIR)/__init__.py | grep __release__ | sed -e 's/^.* = '\"'//' -e 's/'\"'//')
DOMAIN				:= $(PROJECT).nikz.in
DOCTHEME			:= classic

setup:
	@pip3 install -Ur requirements.txt

test: setup
	@python3 ./tests/test_settings.py

clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean: clean-build
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '.DS_Store' -exec rm -rf {} +
	@find . -name 'Thumbs.db' -exec rm -rf {} +

build: clean test
	@pip3 install twine
	@python3 setup.py sdist bdist_wheel

publish: build
	@twine upload dist/*

test-publish: build
	@twine upload --repository testpypi dist/*

rmd:
	@rm -rf $(DOCSDIR)

docs: rmd
	@echo "\nCompiling docs for $(PROJECT) v$(RELEASE)\n"
	@sphinx-apidoc -f -F -e -a -M -l -d 5 -H '$(PROJECT)' -A '$(AUTHOR)' -V '$(VERSION)' -R '$(RELEASE)' -o $(DOCSRCDIR) $(SRCDIR)
	@sed -i "" -e 's/path\.insert\(.*\)$$/path.append\('\''..\/..'\''\)/' -e "s/alabaster/$(DOCTHEME)/" $(DOCSRCDIR)/conf.py

html:
	@cd $(DOCSRCDIR) && make html
	@echo "Moving HTML files to docs directory"
	@cp -af $(DOCSRCDIR)/_build/html/. $(DOCSDIR)
	@echo "Removing source"
	@rm -rf $(DOCSRCDIR)
	@echo "Configuring docs for Github pages"
	@echo '$(DOMAIN)' > $(DOCSDIR)/CNAME
	@echo "Documentation successfully created."
	@touch $(DOCSDIR)/.nojekyll

html-docs:
	@make docs
	@make html

run: setup
	@python3 ./example/app.py

.PHONY:
	setup
	test
	clean-build
	clean
	build
	publish
	test-publish
	rmd
	docs
	html
	html-docs
	run
