"""
Tests for {{ cookiecutter.import_name }}.utils.py
"""
############
# Standard #
############
import inspect
import logging
from pathlib import Path
from collections.abc import Iterable

###############
# Third Party #
###############
import pytest
import numpy as np

##########
# Module #
##########
from {{ cookiecutter.import_name }} import utils

logger = logging.getLogger(__name__)

test_values = [2, np.pi, True, "test_s", "10", ["test"], ("test",), {"test":1}]
test_lists = [[1,2,3,4,5], [[1],[2],[3],[4],[5]], [[1,2,3],[4,5]],
              [[1,[2,[3,[4,[5]]]]]]]

def get_objects_in_module(module, cls=None):
    objects = []
    all_objects = inspect.getmembers(module)
    for _, obj in all_objects:
        if cls is not None:
            try:
                if not isinstance(obj, cls):
                    continue
            except TypeError:
                continue
        objects.append(obj)
    return objects

test_dir_paths_and_names = [(p, "/".join(p.parts[-2:])) for p in
                             get_objects_in_module(utils, Path)]

@pytest.mark.parametrize("test", test_values)
def test_isiterable_correctly_returns(test):
    iterable = utils.isiterable(test)
    if isinstance(test, str):
        assert iterable is False
    elif isinstance(test, Iterable):
        assert iterable is True
    else:
        assert iterable is False

@pytest.mark.parametrize("test", test_lists)
def test_flatten_works_correctly(test):
    assert utils.flatten(test) == [1,2,3,4,5]

@pytest.mark.parametrize("path,name", test_dir_paths_and_names)
def test_importable_dirs_exist(path, name):
    assert path.exists()
    
