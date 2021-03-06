#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
#
# wavestate documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 15 21:40:50 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
"""
#import sys
import os
import re

import inspect
import importlib
from wavestate.sphinx import ws_parse_cov_html

# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'nbsphinx',
    "sphinx_toolbox.assets",
    "sphinx_toolbox.code",
    "sphinx_toolbox.decorators",
    "sphinx_toolbox.collapse",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    'sphinx.ext.autosectionlabel',
    # "sphinx.ext.linkcode",
    "wavestate.sphinx.linkcode_ws",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "docs/index"

# General information about the project.
project = "wavestate"
copyright = "2022, Lee McCuller"
author = "Lee McCuller"
show_authors = False

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import wavestate.collection

version = wavestate.collection.__version__
# The full version, including alpha/beta/rc tags.
release = wavestate.collection.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "**.ipynb_checkpoints", "testing"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# pygments_style = 'colorful'
pygments_style = "default"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Autodoc settings
autodoc_default_flags = ["members", "undoc-members"]

# -- Options for sourcelinks
srclink_project = "https://github.com/wavestate/wavestate"
srclink_src_path = "src/wavestate/"
srclink_branch = "main"

# -- Options for HTML output ----------------------------------------------

# useful for downloading the ipynb files
html_sourcelink_suffix = ""


html_title = "wavestate documentation"
html_short_title = "wavestate"
#html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = dict(
    description="Documentation for the wavestate physics toolkit",
    extra_nav_links={
        #'LIGO CDS repository' : 'https://git.ligo.org/CDS/dttxml'
    },
    show_powered_by=False,
    show_related=True,
    page_width='auto',


)

# options for sphinx_rtd_theme
html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 5,
    'includehidden': True,
    'titles_only': False
}

napoleon_type_aliases = {
    # "CustomType": "mypackage.CustomType",
    # "dict-like": ":term:`dict-like <mapping>`",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "about.html",
        'globaltoc.html',
        "navigation.html",
        "relations.html",
        "searchbox.html",
    ],
    #    'index': [
    #        'globaltoc.html',
    #        'navigation.html',
    #        'relations.html',
    #        'searchbox.html',
    #        'srclinks.html',
    #        ],
}



# Output file base name for HTML help builder.
htmlhelp_basename = "wavestate"

html_logo = 'docs/logo/logo_ws_block.svg'


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return "https://github.com/wavestate/wavestate/%s.py" % filename


autosummary_generate = True
autosummary_imported_members = False
autosummary_generate_overwrite = True

autodoc_mock_imports = [
    "pygraphviz",
    "pcaspy",
    "control",
]

python_use_unqualified_type_names = True

add_module_names = False
show_authors = True

# TODO, change this. Currently should point to srcdir
assets_dir = '.'

coverage_folder = './testing/test_results/coverage/'
test_results_folder = 'testing/test_results'

try:
    coverage_d = ws_parse_cov_html.parse_cov_index(os.path.join(coverage_folder, 'index.html'))
except Exception:
    coverage_d = None

def linkcode_ws_resolve(domain, info):
    if domain != 'py':
        return {}
    if not info['module']:
        return {}
    #print("INFO: ", info)
    module = info['module']
    fullname = info.get('fullname', None)
    filename = module.replace('.', '/')
    d = {}

    def lno(pre):
        fileline = None
        try:
            mod = importlib.import_module(module)
            obj = mod
            for name in fullname.split('.'):
                obj = getattr(obj, name, None)
                if obj is None:
                    break
            if obj is not None:
                codelines, fileline = inspect.getsourcelines(obj)
        except Exception:
            fileline = None
        if fileline is None:
            return ''
        else:
            return '#{}{}'.format(pre, fileline)

    if coverage_d is not None:
        pyfname = filename + '.py'
        cov_fname = coverage_d.get(pyfname, None)
        if cov_fname is not None:
            # converted to output relative to the outdir
            # cov_fpath = os.path.join('/', coverage_folder, cov_fname)
            # converted to output relative to the srcdir
            # needs the double __ since one gets removed by Sphinx.
            # Seems fragile but works for now
            cov_fpath = os.path.join(r'/_static/coverage/', cov_fname)
            d['cov'] = cov_fpath + lno('t')


    if module.startswith('wavestate.quantum'):
        d['github'] = "https://github.com/wavestate/wavestate-quantum/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.bunch'):
        d['github'] = "https://github.com/wavestate/wavestate-bunch/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.pytest'):
        d['github'] = "https://github.com/wavestate/wavestate-pytest/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.utilities'):
        d['github'] = "https://github.com/wavestate/wavestate-utilities/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.declarative'):
        d['github'] = "https://github.com/wavestate/wavestate-declarative/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.LIGO.IFO'):
        d['git.ligo'] = "https://git.ligo.org/wavestate/wavestate-LIGO-IFO/-/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.control'):
        d['github'] = "https://github.com/wavestate/wavestate-control/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.model'):
        d['github'] = "https://github.com/wavestate/wavestate-model/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.iirrational'):
        d['github'] = "https://github.com/wavestate/wavestate-iirrational/tree/main/src/%s.py" % filename + lno('L')
    elif module.startswith('wavestate.AAA'):
        d['github'] = "https://github.com/wavestate/wavestate-AAA/tree/main/src/%s.py" % filename + lno('L')
    elif module.lower().startswith('gwinc'):
        d['git.ligo'] = "https://git.ligo.org/gwinc/pygwinc/-/tree/master/gwinc/%s.py" % filename + lno('L')
    else:
        pass

    return d

def linkcode_resolve(domain, info):
    """in case linkcode is working but linkcode_ws is not
    """
    return linkcode_ws_resolve(domain, info)[1]


def autodoc_process_docstring(app, what, name, obj, options, lines):
    """Detects pytests and augments their documentation to include links to their output files
    """
    tdirs = [
        os.path.join(app.srcdir, test_results_folder),
        # currently disabling other test pulls
        # so that the workflow is "pristine"
        # os.path.join(app.srcdir, 'test_archive'),
    ]

    def istest_check(fname):
        istest = False
        for tdir in tdirs:
            tpath = os.path.join(tdir, fname)
            if os.path.exists(tpath):
                istest = True
                break
        return istest, tpath

    def get_relpath_root(fpath, other):
        source_path = os.path.relpath(fpath, app.srcdir)
        source_path_inv_pre = os.path.relpath(app.srcdir, app.outdir)
        source_path_inv_src = os.path.relpath(source_path_inv_pre, source_path)
        source_path_inv_out = os.path.relpath('.', source_path)

        if other.startswith('/'):
            if other.startswith('//'):
                other = os.path.join(source_path_inv_src, other[2:])
                internal = True
            else:
                other = os.path.join(source_path_inv_out, other[1:])
                internal = True
        else:
            internal = False
        other = other.replace('_', r'\_')
        return other

    if what == 'module':
        # this determines if the module is a test-containing module
        # could also just check if it corresponds to a folder in test_results
        # or better yet, check if it has been run
        ofile = getattr(obj, '__file__', None)
        fpath, fname = os.path.split(ofile)
        istest, tpath = istest_check(fname)
        if hasattr(obj, 'tpath_join'):
            if not istest:
                lines.append("This is a pytest, but its test folder is missing. Some of the annotations of the tests may be missing.")
            # print("MOD-lines: ", lines)
            istest = True

        # print("CHECK: ", ofile, istest)
        if istest:
            if not lines:
                lines.append("")
                lines.append("This is a pytest module needing documentation")
                lines.append("")
            reportname = '/_static/reports/all/{}'.format(fname.replace('.py', '.html'))
            lines.append(r"Report in `report <{}>`__".format(get_relpath_root('_autosummary/name/', reportname)))
        return

    if what != 'function':
        return

    try:
        ofile = obj.__code__.co_filename
    except AttributeError:
        return

    # check for unusual objects like DeepBunch
    if not isinstance(ofile, str):
        return

    fpath, fname = os.path.split(ofile)

    istest, tpath = istest_check(fname)
    # Note that the following code relies on tpath being set after the break

    tname = obj.__name__.split('.')[-1]
    # could also check if the containing module has pytest fixtures, but this seems to work

    if istest:
        # print("FOUND A TEST: ", name)
        # raise Exception("EXPLODE")
        tdirs = os.listdir(tpath)
        mydirs = []

        for subdir in tdirs:
            if '[' not in subdir:
                if subdir == tname:
                    mydirs.append(subdir)
            else:
                if re.fullmatch(re.escape(tname)+r'\[.*\]', subdir):
                    mydirs.append(subdir)

        if not lines:
            lines.append("This is a pytest needing documentation")
            lines.append("")
            lines.append("")

        if mydirs:
            # print("COOL", mydirs)
            pass

        for d in mydirs:
            dpath = os.path.join(tpath, d)
            lines.append("")
            lines.append(".. collapse:: {}".format(d))
            #TODO do some image conversion
            # possibly using https://www.sphinx-doc.org/en/master/usage/extensions/imgconverter.html
            # i.e. check if pdf is a single page, then have imgconvert rasterize it to directly include within the collapse
            lines.append("           ")
            for fpath in ordered_test_outputs(dpath):
                #lines.append("    * :download:`{}</{}>`".format(fpath, os.path.relpath(os.path.join(dpath, fpath), app.srcdir)))
                #lines.append("    * :download:`{}</{}>`".format(fpath, os.path.relpath(os.path.join(dpath, fpath), app.srcdir)))
                print("CHECK", os.path.relpath(os.path.join(dpath, fpath), os.path.abspath(test_results_folder)))
                rp = get_relpath_root('_autosummary/name/', os.path.join('/_static/test_results/', os.path.relpath(os.path.join(dpath, fpath), os.path.abspath(test_results_folder))))
                print("relpath: ", fpath, rp)
                lines.append(r"    * `{} <{}>`__".format(fpath, rp))
            lines.append("")
        # print("OUT: ", name)
    return


def ordered_test_outputs(dpath):
    files = os.listdir(dpath)

    files.sort(key=lambda f: os.stat(os.path.join(dpath, f)).st_mtime)

    capname = 'capture.txt'
    if capname in files:
        files.remove(capname)
        # reinsert at the beginning
        files[0:0] = [capname]

    return files


def setup(app):
    app.add_css_file("my_theme.css")
    app.add_css_file("pygments_adjust.css")

    # add the evennt handler to bond tests to their outputs
    app.connect('autodoc-process-docstring', autodoc_process_docstring)
    return

