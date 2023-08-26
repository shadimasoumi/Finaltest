# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DEMO'
copyright = '2023, X'
author = 'X'
import os
import sys
release = '0.1'
version = '0.1.0'


# -- General configuration
sys.path.insert(0, os.path.abspath('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages'))
import sphinx_rtd_theme



matlab_src_dir = os.path.dirname(os.path.abspath(__file__))
matlab_show_property_default_value = True
matlab_short_links = True

extensions = [
    'sphinx.ext.viewcode',   
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinxcontrib.matlab',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
   
]

primary_domain = "mat"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
