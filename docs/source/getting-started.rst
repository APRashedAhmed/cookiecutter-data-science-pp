Getting Started
===============

Once the project has been made, there are some initial setup steps before
starting development.

Setting up the conda environment
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
