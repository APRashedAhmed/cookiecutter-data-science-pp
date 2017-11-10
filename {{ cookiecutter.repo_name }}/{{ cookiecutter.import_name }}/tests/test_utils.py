"""
Tests for pyutils.pyutils
"""
############
# Standard #
############
import logging
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
test_dir_paths = [
    utils.DIR_REPO, utils.DIR_DATA_EXT, utils.DIR_DATA_INT, utils.DIR_DATA_PROC,
    utils.DIR_LOGS, utils.DIR_NOTEBOOKS,
]

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

@pytest.mark.parametrize("dir_path", test_dir_paths)
def test_importable_dirs_exist(dir_path):
    assert dir_path.exists()

    
