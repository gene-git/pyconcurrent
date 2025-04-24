# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pyconcurrent"
copyright = '2025, Gene C'
author = 'Gene C'
release = '1.3.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['myst_parser']
extensions = ['myst_parser', 'sphinx.ext.autodoc', 'autoapi.extension']

autoapi_dirs = ['../src/pyconcurrent']
#autoapi_options = ['members', 'show-module-summary']
autoapi_options = ['members', 'inherited-members']
autoapi_keep_files = True
add_module_names = False
autoapi_member_order = 'groupwise'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

def skip_submodules(app, what, name, obj, skip, options):
    skip = True
    if name in ('ProcRunMp', 'ProcRunAsyncio', 'ProcResult'):
        skip = False

    if what == 'class' and name.endswith('__init__'):
        skip = False

    return skip

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
