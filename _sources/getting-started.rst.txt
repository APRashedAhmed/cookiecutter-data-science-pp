Getting Started
===============

Once the project has been made, there are some initial setup steps before
starting development.

Setting Up the Conda Environment
--------------------------------

First create the development environment that will have all the packages. The
easiest way to do this is by running make with the following command: ::

  $ make conda-env

This will create an environment with the same name as the project's import name.
The packages that will be installed a combination of what is listed in
``requirements.txt`` and ``dev-requirements.txt``.


Add to Github Remote Repo
-------------------------

Navigate to your github page and create the remote repo. Source a conda
environment that has ``versioneer`` installed. 

From the top level directory run the following command to add all the relevant
files to the remote repo: ::

  $ make github

This will add all the relevant files to git and then push them to the remote
repo.

Online Development Tools
------------------------

There are three primary development tools that the cookiecutter works with out
of the box:

- `travis-ci <https://docs.travis-ci.com/>`_ - Continuous integration
- `codcov <https://codecov.io/?>`_ - Code coverage
- `codacy <https://www.codacy.com/>`_ - Code Quality

Each of these tools have a corresponding dot file at the top level directory of
the project which can be modified.

To actually use these tools, first add the project to github (manually or using
the commands above), and then navigate to each of the links above and set up the
project. Each one has its own process but they are all generally painless.

.. note:: Free versions of these tools generally require the repo be set to
   public
