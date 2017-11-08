############
# Standard #
############
import os
import shutil

###############
# Third Party #
###############
import pytest
from cookiecutter import main

CCDS_ROOT = os.path.abspath(
                os.path.join(
                    __file__,
                    os.pardir,
                    os.pardir
                )
            )

@pytest.fixture(scope='function')
def default_baked_project(tmpdir):
    out_dir = str(tmpdir.mkdir('data-project'))

    main.cookiecutter(
        CCDS_ROOT,
        no_input=True,
        extra_context={},
        output_dir=out_dir
    )

    # default project name is project_name
    yield os.path.join(out_dir, 'project_name')

    # cleanup after
    shutil.rmtree(out_dir)

# Test the folders were created properly
    
def test_folders(default_baked_project):
    expected_dirs = [
        'data',
        os.path.join('data', 'external'),
        os.path.join('data', 'interim'),
        os.path.join('data', 'processed'),
        os.path.join('data', 'raw'),
        'docs',
        os.path.join('figures', 'finalized'),
        os.path.join('figures', 'unsorted'),
        'logs',
        'models',
        'notebooks',
        'references',
        'src',
        os.path.join('src', 'data'),
        os.path.join('src', 'features'),
        os.path.join('src', 'models'),
        os.path.join('src', 'visualization')
    ]

    ignored_dirs = [
        default_baked_project
        ]

    abs_expected_dirs = [os.path.join(default_baked_project, d) for
                            d in expected_dirs]

    abs_dirs, _, _ = list(zip(*os.walk(default_baked_project)))

    assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0

def no_curlies(filepath):
    """
    Utility to make sure no curly braces appear in a file. That is, was jinja
    able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)

# Test all the top level files were created propertly

expected_files = [
    '.coveragerc',
    '.gitignore',
    '.landscape.yml',
    '.travis.yml',
    'LICENSE',
    'Makefile',
    'MANIFEST.in',
    'README.rst',
    'requirements.txt',
    'run_tests.py',
    'setup.py',
    'setup.cfg',
    'versioneer.py',
    os.path.join('src', '__init__.py'),
    os.path.join('src', 'data', '__init__.py'),
    os.path.join('src', 'data', 'make_dataset.py'),    
    os.path.join('src', 'features', '__init__.py'),
    os.path.join('src', 'features', 'build_features.py'),    
    os.path.join('src', 'models', '__init__.py'),
    os.path.join('src', 'models', 'predict_model.py'),
    os.path.join('src', 'models', 'train_model.py'),    
    os.path.join('src', 'visualization', '__init__.py'),
    os.path.join('src', 'visualization', 'visualize.py'),    
    ]

@pytest.mark.parametrize("expected_file", expected_files)
def test_file(default_baked_project, expected_file):
    path_expected_file = os.path.join(default_baked_project, expected_file)
    assert os.path.exists(path_expected_file)
    assert no_curlies(path_expected_file)


