import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'pysweph'
copyright = '2026 sailorfe'
author = 'sailorfe'
version = '0.1.0'
release = '0.1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

exclude_patterns = ['_build']

html_theme = 'shibuya'


autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
    'no-inherited-members': True,
}

toc_object_entries = False
