# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, '..')

# -- Project information -----------------------------------------------------

project = 'pi-clap'
copyright = '2020, Nikhil John'
author = 'Nikhil John'
version = '1.1'
release = '1.1.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
highlight_language = 'python'
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

html_theme = 'classic'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

todo_include_todos = True
