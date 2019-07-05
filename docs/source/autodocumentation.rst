Auto-Documentation
==================

The documentation setup for the cookiecutter relies on a combination of the
following tools:

- `travis-ci <https://docs.travis-ci.com/>`_
- `sphinx <https://www.sphinx-doc.org/en/master/>`_
- `doctr <https://drdoctr.github.io/>`_

Where sphinx creates the documentation pages, travis-ci builds them, and doctr
deploys them to github pages.

Building Documentation Locally
------------------------------

To test the resulting documentation pages, build them locally and make the
desired changes before pushing them online.

First install the requirements: ::

  $ conda install --file docs-requirements

Depending on the way your documentation is structured you may need to also have
the project in your python path. If it hasn't already been added, run the
following command at the top level directory of the repo: ::

  $ python setup.py develop

Navigate to the documentation directory: ::

  $ cd docs

And then run ``make`` with the desired output. For example, to generate html
pages: ::

  $ make html

This will build the documenation as html pages which will reside in
``docs/_build``. To launch the page, open the index page with a web browser
such as firefox: ::

  $ firefox _build/index.html

Below is a list of all the ``make`` commands (which can also be printed on the
console by running ``make`` with no arguments). ::

  Please use `make <target>' where <target> is one of
    html       to make standalone HTML files
    dirhtml    to make HTML files named index.html in directories
    singlehtml to make a single large HTML file
    pickle     to make pickle files
    json       to make JSON files
    htmlhelp   to make HTML files and a HTML help project
    qthelp     to make HTML files and a qthelp project
    devhelp    to make HTML files and a Devhelp project
    epub       to make an epub
    latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
    latexpdf   to make LaTeX files and run them through pdflatex
    text       to make text files
    man        to make manual pages
    texinfo    to make Texinfo files
    info       to make Texinfo files and run them through makeinfo
    gettext    to make PO message catalogs
    changes    to make an overview of all changed/added/deprecated items
    linkcheck  to check all external links for integrity
    doctest    to run all doctests embedded in the documentation (if enabled)

Travis and Doctr
----------------

.. note:: This section assumes ``travis-ci`` has already been setup

With ``doctr`` installed, run the following from the top level directory: ::

  $ doctr configure

Follow the prompts to identify the user and repo this will be set up for, after
which it will create a deploy key file and provide directions to proceed.

Like what is stated, add the deploy key using git and add the line with the
secure key provided to the ``.travis.yml`` file, but you do **not** have to add
the lines that run the doctr script. More concretely, only add the following
lines: ::

  2. Add these lines to your `.travis.yml` file:
      env:
	global:
	  # Doctr deploy key for <github user/github repo>
	  - secure: "<project key>"

Commit and push the changes to the remote repo and now anytime the master branch
has a commit that successfully passes all the tests, the documentation will be
rebuilt and updated on github pages (assuming the documentation builds as well).
