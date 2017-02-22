import sys
import pathlib
import re


# -- Path setup --------------------------------------------------------------
here = pathlib.Path(__file__).parent.resolve()
sys.path.insert(0, (here / "../../pyrsktools").name)

# -- Project information -----------------------------------------------------

project = "pyRSKtools"
copyright = "2022, RBR"
author = "RBR"
version = re.search(
    r'__version__ = "(.+?)"', (here / "../../pyrsktools/__init__.py").read_text("utf8")
).group(1)
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_toolbox.collapse",
    "sphinx_paramlinks",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_logo = "img/RBR.png"
html_favicon = "img/favicon.ico"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_theme_options = {
    "fixed_sidebar": True,
    "sidebar_width": "300px",
    "page_width": "70%",
    "show_powered_by": False,
}
html_show_sourcelink = False


# -- Options for autodoc  -------------------------------------------------
autodoc_typehints_format = "short"
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_preserve_defaults = True
napoleon_use_rtype = False
