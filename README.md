<h1 align="center">Data Science++ Cookiecutter</h1>
<!-- Pulled from the readme of pcdsdevices https://github.com/pcdshub/pcdsdevices -->

<!-- <p align="center"> -->
<!--   <a href="#motivation">Motivation</a> • -->
<!--   <a href="#installation">Installation</a> -->
<!-- </p> -->

<div align="center">

  <!-- Build Status -->
  <a href="https://travis-ci.org/apra93/cookiecutter-data-science-pp">
  <img alt="Travis (.org)" src="https://travis-ci.org/apra93/cookiecutter-data-science-pp.svg?branch=master">
  </a>

  <!-- License -->
  <a href="https://github.com/apra93/cookiecutter-data-science-pp/blob/master/LICENSE">
  <img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  </a>

</div>
  <!-- Add in a break between the badges and the next section. Will likely not be necessary if there is a header after this -->

<h5 align="center">An Extended data science cookiecutter with engineering tools</h5>

An extension of the standard data science cookiecutter template that adds a number of things I've found to be useful for data-oriented projects. This includes some small scripts and development tools like travis-ci and codecov, among others.

## Original Data Science Coockiecutter

This project is mainly an extension of the main data science cookicutter which can be found here:

- 	[Project Homepage](https://drivendata.github.io/cookiecutter-data-science/)
- 	[Github](https://github.com/drivendata/cookiecutter-data-science/)

## Requirements for the Template

-   Python >= 3.5
-   [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0
-   simplejson

This can be installed with pip by or conda depending on how you manage your Python packages: 

```bash
$ pip install cookiecutter
```

or

```bash
$ conda install cookiecutter -c conda-forge
```

Starting a New Project
----------------------

If you're using this cookiecutter for the first time or are in need of an updated clone:

```bash
$ cookiecutter https://github.com/apra93/cookiecutter-data-science-pp
```

Otherwise:

```bash
$ cookiecutter cookiecutter-data-science-pp
```

## Running Cookiecutter Tests

To test that all the script and generated files, first install the requirements for running the tests and the underlying repo:

```bash
$ conda install --file dev-requirements.txt -c conda-forge
```

And then run the testing script:

```bash
$ python run_tests.py
```

## Some Useful Links

When starting new projects the following pages could be useful:

-   [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
-   [Markdown online editor](https://jbt.github.io/markdown-editor/)
-   [reStructuredText cheatsheet](https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst)
-   [reStructuredText online editor](http://rst.ninjs.org/)
-   [Shields.io](https://shields.io/)
