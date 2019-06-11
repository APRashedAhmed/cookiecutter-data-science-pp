.. {{ cookiecutter.project_name }} documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. mdinclude:: ../../README.md

   
Contents:

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting-started
   commands

.. toctree::
   :maxdepth: 2
   :caption: Reports
   :glob:
	 
   reports/*	    

.. toctree::
   :maxdepth: 2
   :caption: Scripts

   data
   features
   models
   visualization
   utils

.. toctree::
   :maxdepth: 1
   :caption: Notebooks
   :glob:
	 
   notebooks/*	     

.. toctree::
   :hidden:
   :caption: Project Links

   Home <https://apra93.github.io/{{ cookiecutter.project_name }}/>
   Github <https://github.com/apra93/{{ cookiecutter.project_name }}/>
   Travis CI <https://travis-ci.org/apra93/{{ cookiecutter.project_name }}>
   Codecov <https://codecov.io/gh/apra93/{{ cookiecutter.project_name }}>
   Codacy <https://app.codacy.com/project/apra93/{{ cookiecutter.project_name }}/dashboard>	     

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
