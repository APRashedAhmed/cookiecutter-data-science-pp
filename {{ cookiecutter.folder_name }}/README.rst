===============================
{{ cookiecutter.project_name }}
===============================
{% if cookiecutter.open_source_license == 'MIT' %}

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/blob/master/LICENSE
{% elif cookiecutter.open_source_license == 'BSD' %}

.. image:: https://img.shields.io/badge/license-BSD-blue.svg
   :target: https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.repo_name }}/blob/master/LICENSE
{% endif %}

{{ cookiecutter.description }}

Requirements
------------

Describe the project requirements (i.e. Python version, packages and how to install them)

Installation
------------

Describe the installation procedure

Running the Tests
-----------------
::

  $ python run_tests.py
   
Directory Structure
-------------------

This repo is based on two cookiecutter templates. See the following github pages for more info:

- `cookiecutter-data-science-pp <https://github.com/apra93/cookiecutter-data-science-pp>`_
- `cookiecutter-data-science <https://github.com/drivendata/cookiecutter-data-science>`_
 
