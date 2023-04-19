"""Sphinx configuration."""
project = "jmpytools"
author = "Jeff Maxey"
copyright = "2023, Jeff Maxey"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
