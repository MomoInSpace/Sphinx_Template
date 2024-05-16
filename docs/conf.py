# Configuration file for the Sphinx documentation of EasyGems
import os
import glob
import fnmatch
import subprocess

# -- Project information -----------------------------------------------------

project = "Sphinx-Notes"
copyright = "2022 MomoInSpace"
author = "MomoInSpace"
project_url = "."


# -- Path setup --------------------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Final Path of css-files: _static/css/...
html_css_files = ["css/footer.css"]


# -- Extensions ---------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    # 'nbsphinx',
    # "sphinx_sitemap",           # Sitemap
    'sphinx.ext.intersphinx',   # Used for Connecting Different Sphinx-Documentations
    # "sphinxext.rediraffe",      # Used to redirect non-existent/old pages to working pages
    "myst_nb",                  # Markdown with Myst
    "sphinx.ext.mathjax",
]

# -- General configuration --------------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# The theme to use for HTML and HTML Help pages.
# Link: https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html
html_theme = "pydata_sphinx_theme"

# Specifying the suffix for various extensions. (MySt, jupyter_sphinx)
source_suffix = {
    '.rst': 'restructuredtext',
    # '.md': 'myst_with_inline_math',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
# exclude all markdown files which are also ipynb files to prevent false warnings
exclude_patterns += [fn.replace(".ipynb", ".md")
                     for fn in glob.glob("**/*.ipynb", recursive=True)]



# -- Theme Configuration -------------------------------------------------------------

# Logo appearing top left on the page
html_logo = '_static/logos/Notes.png'

# Used for the "edit"-button:
html_context = {
   "gitlab_url": "https://github.com",
   "gitlab_user": "MomoInSpace",
   "gitlab_repo": "SphinxNotes",
   "gitlab_version": "main/source",
   # "doc_path": "https://gitlab.dkrz.de",
}

# Configuration for the left sidebar
html_sidebars = {
    "**": [
        "search-field",
        "sidebar-nav-bs",
    ],
}

# Configuration for the PyData Theme
html_theme_options = {
    # "external_links": [
    #     {"url": "https://www.dkrz.de/de/about/kontakt/impressum", "name": "Legal"},
    #     {"url": "https://www.dkrz.de/en/about-en/contact/en-datenschutzhinweise", "name": "Privacy"},
    # ],
    # "github_url": "https://github.com/MomoInSpace/SphinxNotes",
    # "twitter_url": "https://twitter.com/........",

    # More Icons: https://fontawesome.com/
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/pydata-sphinx-theme",
            "icon": "fas fa-box",
        },
    ],
    # "use_edit_page_button": True,
    "show_toc_level": 1,
    # "show_nav_level": 2,
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "navbar_start": ["navbar-logo", "navbar-version"],
    # "navbar_center": ["navbar-nav", "navbar-version"],  # Just for testing
    "navbar_end": ["navbar-icon-links"],
    # "footer_items": ["sbt-sidebar-footer","copyright", "sphinx-version"]
    "footer_start": ["custom-footer"],
    # Configure with keys:
    "navigation_with_keys": True
}


# -- Extension Configuration ----------------------------------------------------------------

# .. nbsphinx ............................................

nbsphinx_custom_formats = {
    ".md": ["jupytext.reads", {"fmt": "mystnb"}],
}

# .. Intersphinx .........................................
intersphinx_mapping = {
        #'dkrz': ('https://doc.dkrz.de/', None),
        # 'jph': ('https://jupyterhub.gitlab-pages.dkrz.de/jupyterhub-docs/', None),
        #'vis': ('https://visualisation.gitlab-pages.dkrz.de/documentation/', None),
        #'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
        "numpy" :("https://numpy.org/doc/stable/", None),
        'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
        'matplotlib': ('https://matplotlib.org/stable/',None),
}
myst_url_schemes = ['http','https', ]

# .. Rediraffe ..........................................
# rediraffe_redirects = "redirects.txt"  # dic containing old pages and their redirected pages
# rediraffe_branch = "main~1"            # ensures that deleted/renamed files are in the repo

# .. Myst_nb ............................................. 
nb_execution_mode = 'off'

# Mathjax
mathjax3_config = {
        'extensions': ['tex2jax.js'],
        'jax': ['input/TeX', 'output/HTML-CSS'],
       'tex2jax': {
           'inlineMath': [['$', '$'], ['\\(', '\\)']],
           'displayMath': [['$$', '$$'], ['\\[', '\\]']],
       },
        }
# mathjax3_config = {
#        'jax': ['input/TeX', 'output/HTML-CSS'],
#        'tex2jax': {
#            'inlineMath': [['$', '$'], ['\\(', '\\)']],
#            'displayMath': [['$$', '$$'], ['\\[', '\\]']],
#        },
#        'HTML-CSS': {
#            'styles': {
#                '.MathJax_Display': {'margin': 0},
#                '.MathJax': {'color': 'black'}
#            }
#        }
#    }

# -- Type of current branch detection -------------------------------------------------------

# running_in_ci = os.environ.get("GITLAB_CI", "false") == "true"
# if running_in_ci:
#     try:
#         merge_request_iid = int(os.environ["CI_MERGE_REQUEST_IID"])
#     except (KeyError, ValueError):
#         merge_request_iid = None
#     if merge_request_iid is not None:
#         merge_request_approved = os.environ.get("CI_MERGE_REQUEST_APPROVED", "false") == "true"
#         commit_branch = os.environ["CI_MERGE_REQUEST_SOURCE_BRANCH_NAME"]
#         merge_request_title = os.environ["CI_MERGE_REQUEST_TITLE"]
#     else:
#         commit_branch = os.environ["CI_COMMIT_REF_NAME"]
#     commit_sha = os.environ["CI_COMMIT_SHA"]
#     default_branch = os.environ["CI_DEFAULT_BRANCH"]
#     gitlab_project_url = os.environ["CI_PROJECT_URL"]
#
#     if merge_request_iid is not None:
#         print(f"building for MERGE REQUEST {merge_request_iid}")
#         # in merge request
#         rst_prolog = f"""
# .. warning::
#    This version of {project} was built within Merge Request |MR{merge_request_iid}|_ ({merge_request_title}) for revision |{commit_sha[:8]}|_.
#    You can find the most recent release version of {project} at {project_url}.
#
# .. |MR{merge_request_iid}| replace:: ``!{merge_request_iid}``
# .. _MR{merge_request_iid}: {gitlab_project_url}/-/merge_requests/{merge_request_iid}
#
# .. |{commit_sha[:8]}| replace:: ``{commit_sha[:8]}``
# .. _{commit_sha[:8]}: {gitlab_project_url}/-/commit/{commit_sha}
# """
#     elif default_branch != commit_branch:
#         print(f"building for BRANCH {commit_branch}")
#         # in non-MR branch
#         rst_prolog = f"""
# .. warning::
#    This version of {project} was built within branch |{commit_branch}|_ for revision |{commit_sha[:8]}|_.
#    You can find the most recent release version of {project} at {project_url}.
#
# .. |{commit_branch}| replace:: ``{commit_branch}``
# .. _{commit_branch}: {gitlab_project_url}/-/tree/{commit_branch}
#
# .. |{commit_sha[:8]}| replace:: ``{commit_sha[:8]}``
# .. _{commit_sha[:8]}: {gitlab_project_url}/-/commit/{commit_sha}
# """
#     else:
#         # in default branch
#         rst_prolog = ""
# else:
#     # running locally
#     rst_prolog = ""
#
# if rst_prolog:
#     print("the following prolog will be prepended:")
#     print(rst_prolog)

print("Converting Latex to rst:========================================================")

def get_files_with_later_timestamp(directory):
    tex_files = []
    for root, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            if fnmatch.fnmatch(file_name, '*.tex'):
                # print(file_name)
                tex_path = os.path.join(root, file_name)
                rst_path = os.path.join(root, file_name[:-3] + 'rst')
                # print(f"Tex time: {os.path.getmtime(tex_path)}")
                # print(f"rst time: {os.path.getmtime(rst_path)}")
                if (os.path.exists(rst_path) and os.path.getmtime(rst_path) < os.path.getmtime(tex_path)) or not os.path.exists(rst_path):
                    tex_files.append(tex_path)
                    # print(f"{tex_path} {rst_path} {root}")
                    # print("Files:")
                    # print("Subprocess:")
                    pdf_filepath = os.path.join(root,"tex_pdf")
                    pdf_filepath =os.path.join(pdf_filepath, file_name[:-3] + 'pdf')
                    print(f"PDF FILEPATH: {pdf_filepath}")
                    print(subprocess.run([f"{directory}_static/scripts/conversion.sh {tex_path} {rst_path} {root} {pdf_filepath}"],shell=True))
    return tex_files

# Example usage:
directory_path = './'
tex_files = get_files_with_later_timestamp(directory_path)
print("DONE===========================================================================")
# print("FILES:===========")
# for tex_file in tex_files:
