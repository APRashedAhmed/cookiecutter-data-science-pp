Resulting Directory Structure
-----------------------------

The directory structure below is heavily influenced by the setup laid out
`here <https://drivendata.github.io/cookiecutter-data-science/#why-use-this-project-structure>`_.

.. code-block:: text

  ├── .codacy                 <- Codacy file for code quality
  │
  ├── .codecov                <- Codecov file when checking coverage
  │
  ├── .github                 <- Directory for github issues and PR templates
  │
  ├── .gitignore              <- Gitignore for the repo
  │
  ├── .travis.yml             <- Yaml file for travis continuous integration
  │
  ├── {{ import_name }}       <- Source code for use in this project.
  │   │
  │   ├── __init__.py         <- Makes src a Python module
  │   │
  │   ├── data                <- Scripts to download or generate data
  │   │
  │   ├── features            <- Scripts to turn raw data into features for
  │   │		                 modeling
  │   │
  │   ├── models              <- Scripts to train models and then use trained 
  │   │                          models to make predictions
  │   │
  │   ├── utils.py            <- Utility functions used throughout the repo
  │   │
  │   └── visualization       <- Scripts to create exploratory and results
  │       		         oriented visualizations
  ├── data
  │   ├── external            <- Data from third party sources
  │   ├── interim             <- Intermediate data that has been transformed
  │   ├── processed           <- The final, canonical data sets for modeling
  │   └── raw                 <- The original, immutable data dump
  │
  ├── dev-requirements.txt    <- The requirements file project development
  │                         
  ├── docs                    <- A default Sphinx project; see sphinx-doc.org
  │		                 for details
  │   
  ├── docs-requirements.txt   <- The requirements file for generating the
  │   				 sphinx documentation		
  │                         
  ├── figures
  │   ├── finalized           <- Figures that have been polished and should not
  │   │ 			 be changed
  │   └── unsorted            <- Unsorted figures that are not version
  │				 controlled
  │
  ├── LICENSE                 <- Licence for the project
  │
  ├── logging.yml             <- Configuration file for the global logger
  │
  ├── logs                    <- Directory for log files and is not  version
  │                              controlled
  │
  ├── Makefile                <- Makefile with commands like `make github` or
  │				 `make versioneer`
  │
  ├── models                  <- Trained and serialized models, model
  │				 predictions, or model summaries
  │
  ├── notebooks               <- Explorative jupyter notebooks. Naming 
  │ 				 convention is a number (for ordering) and a
  │		                 short `-` delimited description.
  │
  ├── README.md               <- The top-level README for developers using this
  │				 project
  │
  ├── references              <- Data dictionaries, manuals, and all other
  │	 			 explanatory materials
  │
  ├── reports                 <- Finalized jupyter notebooks
  │
  ├── requirements.txt        <- The requirements file for reproducing the
  │ 				 analysis environment
  │
  ├── run_tests.py            <- Script that runs the files in the tests
  │   				 directory
  │
  ├── setup.cfg               <- Setup file for versioneer
  │
  └── setup.py                <- `setup.py` file configured to use versioneer
