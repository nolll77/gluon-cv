# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import guzzle_sphinx_theme

import os
import recommonmark
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import ExampleTitleSortKey

# -- Project information -----------------------------------------------------

project = 'gluoncv'
copyright = '2018, MXNet Developers'
author = 'MXNet Developers'

# The short X.Y version
import gluoncv as gcv
version = gcv.__version__
release = gcv.__version__

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx_gallery.gen_gallery',
]

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs': [
        'tutorials/datasets',
        'tutorials/classification',
        'tutorials/detection',
        'tutorials/instance',
        'tutorials/segmentation',
        'tutorials/pose',
        'tutorials/action_recognition',
        'tutorials/tracking',
        'tutorials/depth',
        'tutorials/distributed',
        'tutorials/deployment',],
    # path where to save gallery generated examples
    'gallery_dirs': [
        'build/examples_datasets',
        'build/examples_classification',
        'build/examples_detection',
        'build/examples_instance',
        'build/examples_segmentation',
        'build/examples_pose',
        'build/examples_action_recognition',
        'build/examples_tracking',
        'build/examples_depth',
        'build/examples_distributed',
        'build/examples_deployment',],

    'filename_pattern': '.pydisabled',
    'ignore_pattern': 'im2rec.py',
    'expected_failing_examples': [],

    # 'subsection_order': ExplicitOrder(['tutorials/classification',
    #                                    'tutorials/detection',
    #                                    'tutorials/segmentation',
    #                                    'tutorials/datasets']),

    'within_subsection_order': ExampleTitleSortKey,
    'plot_gallery': True,
    'download_section_examples': False,
    'reference_url': {
        'gluoncv': None,
    },
    'backreferences_dir': None,
}

# Disable tutorial if needed
if os.environ.get('GLUONCV_DISABLE_TUTORIALS', 'False').lower() == 'true':
    del sphinx_gallery_conf['filename_pattern']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#

source_parsers = {'.md': CommonMarkParser}
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# Use customize landing page
html_additional_pages = {'index': 'index.html'}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_logo = '_static/gluon-logo.svg'
html_favicon = '_static/gluon.ico'
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'

# # Register the theme as an extension to generate a sitemap.xml
# extensions.append("guzzle_sphinx_theme")

# # Guzzle theme options (see theme.conf for more information)
# html_theme_options = {
#         # Set the name of the project to appear in the sidebar
#         "project_nav_name": "GluonCV",
# }

html_theme = 'mxtheme'
html_theme_path = ['mxtheme']
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links' : [
        ('Install', 'install/install-more', False, ''),
        ('Tutorial', 'tutorials/index', False, ''),
        ('API', 'api/index', False, ''),
        ('Community', 'how_to/support', False, ''),
        ('Contribute', 'how_to/contribute', False, ''),
        ('GitHub', 'https://github.com/dmlc/gluon-cv/', True, 'link'),
    ],

    # custom layout
    'fixed_drawer': True,
    'fixed_header': True,
    'header_waterfall': True,
    'header_scroll': True,

    # Render footer (Default: True)
    'show_footer': False
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GluonCVdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
   (master_doc, 'GluonCV.tex', 'GluonCV Documentation',
     'MXNet Developers', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gluoncv', 'GluonCV Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GluonCV', 'GluonCV Documentation',
     author, 'GluonCV', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'mxnet':('https://mxnet.apache.org/api/python/docs/', None),
    'python':('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'matplotlib': ('http://matplotlib.sourceforge.net/', None)
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

def setup(app):
    import mxtheme
    app.add_directive('card', mxtheme.CardDirective)

    app.add_javascript('google_analytics.js')
    app.add_javascript('hidebib.js')
    app.add_javascript('install-options.js')
    app.add_javascript('tabs.js')
    app.add_stylesheet('css/custom.css')
     #app.add_transform(AutoStructify)
    #app.add_config_value('recommonmark_config', {
    #}, True)
    # app.add_javascript('google_analytics.js')
