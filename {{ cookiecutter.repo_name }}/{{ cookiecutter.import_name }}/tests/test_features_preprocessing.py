"""
Tests for {{ cookiecutter.import_name }}.features.preprocessing.py
"""
############
# Standard #
############
import logging

###############
# Third Party #
###############
import pytest
import numpy as np
import pandas as pd

##########
# Module #
##########
from {{ cookiecutter.import_name }}.features import preprocessing

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("bad_value", [np.inf, -np.inf, np.nan])
def test_remove_nan_inf(bad_value):
    for i in range(5):
        df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10])        
        df[:i] = bad_value
        df_replaced = df.replace([np.inf, -np.inf], np.nan)
        df_clean = preprocessing.remove_nan_inf(df, reindex=False)
        df_clean_replaced = df_clean.replace([np.inf, -np.inf], np.nan)
        assert df_replaced.isnull().values.any()
        assert not df_clean_replaced.isnull().values.any()
        assert len(df_clean_replaced == len(df)-i)
