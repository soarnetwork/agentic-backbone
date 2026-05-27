# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime

# Add project root to sys.path if needed for autodoc later.
sys.path.insert(0, os.path.abspath(".."))

project = "agentic-backbone"
author = "SourNetwork"
release = "0.1.0"
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_title = "agentic-backbone Documentation"
html_theme_options = {
    "sidebar_hide_name": True,
}

# Enable todo items in build using -D todo_include_todos=1
todo_include_todos = True

# General information used by the documentation.
html_last_updated_fmt = "%b %d, %Y"


def setup(app):
    app.add_css_file("custom.css")
