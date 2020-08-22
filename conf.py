import hackmd
BLOG_TITLE = title = html_title = "Writing docs sucks!"
BLOG_AUTHOR = author = "Quansight"
html_theme = "pydata_sphinx_theme"
master_doc = "index"
source_suffix = ".md .rst .ipynb .py".split()
extensions = (
    "myst_parser nbsphinx sphinx.ext.autodoc sphinx.ext.napoleon".split()
)  # autoapi.extension
exclude_patterns = ["_build", "*checkpoint*", "output", "outputs"]
autoapi_type = "python"
autoapi_dirs = []
THEME = "material-theme"
DEFAULT_LANG = "en"


NAVIGATION_LINKS = {
    DEFAULT_LANG: tuple(),
}

THEME_COLOR = "#7B699F"

POSTS = (
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
    ("posts/*.ipynb", "posts", "post.tmpl"),
    ("posts/*.md.ipynb", "posts", "post.tmpl"),
)

# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Writing docs sucks!",
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://writingdocssucks.readthedocs.io/",
    # Set the color and the accent color
    "color_primary": THEME_COLOR,
    "color_accent": "light-yellow",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/Quansight/quirkshop-docs",
    "repo_name": "Writing docs sucks!",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
    "nav_links": [
        {"href": "index", "title": "Writing docs sucks!", "internal": True, },
    ],
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Exclude build directory and Jupyter backup files:
exclude_patterns = ["_build", "*checkpoint*", "site", "jupyter_execute"]


latex_documents = [
    (master_doc, "quirkshop-docs.tex",
     "Quirkshop about docs", "quirkshop-docs", "manual",)
]

jupyter_execute_notebooks = "off"
