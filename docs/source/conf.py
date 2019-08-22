#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# qats documentation build configuration file, created by
# sphinx-quickstart on Sat Dec 16 19:53:09 2017.
#
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_bootstrap_theme

sys.path.append(os.path.abspath(os.path.join('..', '..')))

# ----------------------------------------------------------------------------------------------------------------------
# General configuration
# ----------------------------------------------------------------------------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'autoapi.extension',  # ref. https://buildmedia.readthedocs.org/media/pdf/sphinx-autoapi/latest/sphinx-autoapi.pdf
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',  # makes sphinx understand docstrings in numpy and google format
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    # 'numpydoc',
    # 'm2r',
    # 'sphinx.ext.viewcode',  # remove this one to disable code view
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']  # source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'QATS'
copyright = 'DNV GL'
author = 'Per Voie, Erling Lone'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# ----------------------------------------------------------------------------------------------------------------------
# AutoAPI configuration
#   ref.: https://buildmedia.readthedocs.org/media/pdf/sphinx-autoapi/latest/sphinx-autoapi.pdf
# ----------------------------------------------------------------------------------------------------------------------
# autoapi_dirs = ['../../qats']
# autoapi_add_toctree_entry = False     # default: True
# autoapi_root = 'api'
# autoapi_generate_api_docs = False     # default: True
# autoapi_include_summaries = False      # default: False
# autoapi_keep_files = False            # default: False
# autoapi_python_class_content = 'both'   # default: 'class'
# autoapi_options = ['members', 'undoc-members', ]  # 'private-members', 'special-members']
# autoapi_ignore = ['*app*']


# ----------------------------------------------------------------------------------------------------------------------
# HTML output configuration
# ----------------------------------------------------------------------------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = 'img/qats.ico'

# Include sidebar
html_sidebars = {
    '**': ['localtoc.html', ],  # 'relations.html', ],  #'globaltoc.html', 'sourcelink.html', 'searchbox.html']}
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {  # bootstrap theme options
    # Navigation bar title. (Default: ``project`` value)
    # 'navbar_title': "Demo",

    # Tab name for entire site. (Default: "Site")
    # 'navbar_site_name': "Site",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate an arbitrary url.
    'navbar_links': [
        ("Getting started", "getting_started"),
        ("GUI", "gui"),
        ("Examples", "examples"),
        ("API", "api/index"),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,  # False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,  # True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 sh
    # ows all levels.
    'globaltoc_depth': 3,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed :hidden: and non-hidden toctree directives
    # in the same page, or else the build will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': None,

    # Bootswatch  theme (see http://bootswatch.com/ for available themes)
    #
    # Options are nothing (default) or the name of a valid theme such as "united", "cosmo" or "sandstone".
    # Note: value av 'navbar_class' (defined above) will affect the look of the theme
    #
    # 'bootswatch_theme': "cosmo",      # (original theme)
    # 'bootswatch_theme': "cerulean",   # (looks okay)
    # 'bootswatch_theme': "sandstone",  #
    # 'bootswatch_theme': "yeti",       # (looks good, but 'See Also' a bit too intense)
    'bootswatch_theme': "spacelab",   # (looks good, better 'See Also' sections)

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# ----------------------------------------------------------------------------------------------------------------------
# Other configuration options
# ----------------------------------------------------------------------------------------------------------------------
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
# html_static_path = ['_static']
# html_style = 'style.css'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}


# ----------------------------------------------------------------------------------------------------------------------
# Autodoc options
# ----------------------------------------------------------------------------------------------------------------------
# autosummary_generate = True  # what difference does this variable do, actually??
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',  # 'alphabetical', 'groupwise', 'bysource'
    # 'special-members': '__init__',
}
autoclass_content = "both"  # include both class' and __init__ method's docstrings (concatenated)


# ----------------------------------------------------------------------------------------------------------------------
# Autosummary
# ... based on code and inspiration provided by:
#   https://stackoverflow.com/questions/20569011/python-sphinx-autosummary-automated-listing-of-member-functions
#   https://github.com/markovmodel/PyEMMA/blob/devel/doc/source/conf.py#L285
# ----------------------------------------------------------------------------------------------------------------------


# try to exclude deprecated
def skip_deprecated(app, what, name, obj, skip, options):
    if hasattr(obj, "func_dict") and "__deprecated__" in obj.func_dict:
        print("skipping " + name)
        return True
    return skip or False


def setup(app):
    app.connect('autodoc-skip-member', skip_deprecated)
    app.add_stylesheet("custom-todo-style.css")  # also can be a full URL
    try:
        import inspect
        from sphinx.ext.autosummary import Autosummary
        from docutils.parsers.rst import directives
        # import sphinx.ext.autodoc
        # from sphinx.ext.autosummary import get_documenter
        # from sphinx.util.inspect import safe_getattr
        # import re

        class AutoAutoSummary(Autosummary):

            option_spec = {
                'modules': directives.unchanged,
                'functions': directives.unchanged,
                'classes': directives.unchanged,
                'methods': directives.unchanged,
                'properties': directives.unchanged,
                'toctree': directives.unchanged,
            }

            required_arguments = 1

            @staticmethod
            def get_class_members(obj, typ, include_public=None):
                """
                Parameters
                ----------
                obj : object
                    Object (class) to inspect.
                typ : str
                    Type of members requested. Valid options: 'method', 'property'
                include_public : list, optional
                    Methods/attributes to include in public list

                Returns
                -------
                public : list
                    List of public members of requested type.
                items : list
                    List of all members of requested type.
                """
                if include_public is None:
                    include_public = []
                if typ == "method":
                    # enlo, 22.08.2019: it appears not all methods are captured by ismethod() any more;
                    # we therefore need to extract members that predicate True for isfunction() as well.
                    items = [m[0] for m in
                             inspect.getmembers(obj, predicate=lambda x: inspect.ismethod(x) or inspect.isfunction(x))]
                elif typ == "property":
                    items = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isdatadescriptor)]
                else:
                    raise ValueError(f"Invalid value for parameter 'typ': {typ}")
                public = [x for x in items if x in include_public or not x.startswith('_')]
                return public, items

            @staticmethod
            def get_module_members(module, typ=('class', 'function')):
                """
                Parameters
                ----------
                module : module
                    Module to inspect.
                typ : str or list, optional
                    Type of members requested. Valid options: 'class', 'function', 'module'

                Returns
                -------
                members : list
                    List of module members
                """
                if isinstance(typ, str):
                    typ = typ,  # make tuple

                def check(mod, member, mtyp):
                    """
                    Function that returns True if `member` should be included in returned list.
                    The following criteria are used:
                        - classes are included if 'classes' is specified
                        - functions are included if 'functions' is specified
                        - modules are included if 'modules' is specified
                        - classes and functions are only included if they are defined in the module inspected
                        - modules are only included if they are not imported
                    """
                    if (inspect.isclass(member) and 'class' in mtyp) and member.__module__ == mod.__name__:
                        return True
                    if (inspect.isfunction(member) and 'function' in mtyp) and member.__module__ == mod.__name__:
                        return True
                    if (inspect.ismodule(member) and 'module' in mtyp) and member.__package__ in member.__name__:
                        return True
                    return False

                # members = [check(module, m[0], typ) for m in inspect.getmembers(module)]
                members = [m[0] for m in inspect.getmembers(module, predicate=lambda x: check(module, x, typ))]
                return members

            def run(self):
                # check that options doesn't contain invalid combinations
                if ('functions' in self.options or 'classes' in self.options) \
                        and ('methods' in self.options or 'attributes' in self.options):
                    raise Exception("invalid option combination: %s" % self.options)

                # import requested module, or module of requested class
                fullname = self.arguments[0]
                root, name = fullname.rsplit('.', 1)
                r = __import__(root, globals(), locals(), [name])   # root module
                cm = getattr(r, name)                               # class or module
                if inspect.isclass(cm):
                    cm_typ = "class"
                elif inspect.ismodule(cm):
                    cm_typ = "module"
                else:
                    raise TypeError(f"Invalid type for {fullname}: {cm}")

                # debug
                '''
                with open("_abc.txt", "a") as f:
                    f.write(f"run : {fullname}, {cm_typ}\n")
                '''

                if cm_typ == "class":
                    try:
                        r = __import__(root, globals(), locals(), [name])
                        cm = getattr(r, name)

                        self.content = []

                        if 'properties' in self.options:
                            _, props = self.get_class_members(cm, 'attribute')
                            self.content += ["~%s.%s" % (fullname, prop) for prop in props if not prop.startswith('_')]

                        if 'methods' in self.options:
                            _, methods = self.get_class_members(cm, 'method', ['__init__'])

                            self.content += ["~%s.%s" % (fullname, method) for method in methods if
                                             not method.startswith('_')]
                    finally:
                        return super(AutoAutoSummary, self).run()

                elif cm_typ == "module":
                    try:
                        '''
                        functions = [o[0] for o in inspect.getmembers(cm)
                                     if (inspect.isfunction(o[1]) or inspect.isclass(o[1])) and o[1].__module__ == r.__name__]
                        self.content = ["~%s.%s" % (fullname, func) for func in functions if not func.startswith('_')]
                        '''
                        typ = []
                        if 'classes' in self.options:
                            typ.append('class')
                        if 'functions' in self.options:
                            typ.append('function')
                        if 'modules' in self.options:
                            typ.append('modules')

                        members = self.get_module_members(cm, typ=typ)
                        self.content = ["~%s.%s" % (fullname, member) for member in members
                                        if not member.startswith('_')]

                    finally:
                        return super(AutoAutoSummary, self).run()

        app.add_directive('autoautosummary', AutoAutoSummary)
    except BaseException as e:
        raise e
