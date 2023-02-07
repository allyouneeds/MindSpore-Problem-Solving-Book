# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from recommonmark.parser import CommonMarkParser
import sphinx_rtd_theme
source_parsers = {
        '.md': CommonMarkParser,
        }
source_suffix = ['.rst', '.md']
project = 'MindSpore-Problem-Solving-Book'
copyright = '2023, ArthurZhao'
author = 'JichenZhao'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark',
              'sphinx_markdown_tables']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = [sphinx_rtd_theme.get_html_theme_path()]
