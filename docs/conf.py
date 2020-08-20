# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../piclap'))

# -- Project information -----------------------------------------------------

project = 'pi-clap'
copyright = '2020, Nikhil John'
author = 'Nikhil John'
release = '1.1.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

html_theme = 'classic'
html_static_path = ['_static']
