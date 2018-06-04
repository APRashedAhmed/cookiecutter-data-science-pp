# -*- coding: utf-8 -*-
############
# Standard #
############
import logging

###############
# Third Party #
###############
import numpy as np
import pandas as pd

##########
# Module #
##########

logger = logging.getLogger(__name__)

def remove_nan_inf(df, reindex=True):
    """
    Removes all rows that have NaN, inf or -inf as a value, and then optionally
    reindexes the dataframe.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe to remove NaNs and Infs from.

    reindex : bool, optional
        Reindex the dataframe so that there are no missing indices.
        
    Returns
    -------
    df : pd.DataFrame
        Dataframe with all the NaNs and Infs removed.
    """
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    if reindex is True:
        df = df.reset_index(drop=True)
    return df

