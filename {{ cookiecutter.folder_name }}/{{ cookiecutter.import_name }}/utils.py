"""
Script for utility functions in {{ cookiecutter.folder_name }}
"""
############
# Standard #
############
import os
import inspect
import logging
import logging.config
from pathlib import Path
from collections.abc import Iterable
from logging.handlers import RotatingFileHandler

###############
# Third Party #
###############
import yaml
import coloredlogs

logger = logging.getLogger(__name__)


class RotatingFileHandlerRelativePath(logging.handlers.RotatingFileHandler):
    """
    Extension of the filehandler class that appends the current directory to the
    inputted filename. This is so the log files can be found relative to this 
    file rather than from wherever the script is run.
    """
    def __init__(self, filename, *args, **kwargs):
        filename_full = os.path.join(os.path.dirname(__file__), filename)
        super().__init__(filename_full, *args, **kwargs)

def absolute_submodule_path(submodule, cur_dir=inspect.stack()[0][1]):
    """
    Returns the absolute path of the inputted submodule based on an inputted
    absolute path, or the absolute path of this file.

    Parameters
    ----------
    submodule : str or Path
        Desired submodule path.

    cur_dir : str or Path, optional
        Absolute path to use as a template for the full submodule path.

    Returns
    -------
    full_path : str
        Full string path to the inputted submodule.
    """
    dir_parts = Path(cur_dir).parts
    sub_parts = Path(submodule).parts
    base_path = Path(*dir_parts[:dir_parts.index(sub_parts[0])])
    if str(base_path) == ".":
        logger.warning("Could not match base path with desired submodule.")
    full_path = base_path / Path(submodule)
    return str(full_path)

# Define some Path objects to folders within the repo
DIR_REPO = Path(absolute_submodule_path("{{ cookiecutter.folder_name }}/"))
DIR_DATA = DIR_REPO / "data"
DIR_DATA_EXT = DIR_DATA / "external"
DIR_DATA_INT = DIR_DATA / "interim"
DIR_DATA_PROC = DIR_DATA / "processed"
DIR_FIG = DIR_REPO / "figures"
DIR_FIG_FINAL = DIR_FIG / "finalized"
DIR_FIG_UNSORTED = DIR_FIG / "unsorted"
DIR_LOGS = DIR_REPO / "logs"
DIR_NOTEBOOKS = DIR_REPO / "notebooks"

def setup_logging(path_yaml=None, dir_logs=None, default_level=logging.INFO):
    """
    Sets up the logging module to make a properly configured logger.

    This will go into the ``logging.yml`` file in the top level directory, and
    try to load the logging configuration. If it fails for any reason, it will
    just use the default configuration. For more details on how the logger will
    be configured, see the ``logging.yml`` file.

    Parameters
    ----------
    path_yaml : str or Path, optional
        Path to the yaml file.

    dir_logs : str or Path, optional
        Path to the log directory.
        
    default_level : logging.LEVEL, optional
        Logging level for the default logging setup if the yaml fails.
    """
    # Get the yaml path
    if path_yaml is None:
        path_yaml = DIR_REPO / "logging.yml"
    # Make sure we are using Path objects
    else: 
        path_yaml = Path(path_yaml)
    # Get the log directory
    if dir_logs is None:
        dir_logs = DIR_LOGS
    # Make sure we are using Path objects
    else:
        dir_logs = Path(dir_logs)
        
    # Make the log directory if it doesn't exist
    if not dir_logs.exists(): 
        dir_logs.mkdir()

    log_files = ['info.log', 'errors.log', 'debug.log',  'critical.log', 
                 'warn.log']
    for log_file in log_files:
        path_log_file = dir_logs / log_file
        # Make the log files if they don't exist
        if not path_log_file.exists():
            path_log_file.touch()
        # Set permissions to be accessible to everyone
        if path_log_file.stat().st_mode != 33279:
            path_log_file.chmod(0o777)        

    # Set up everything if the yaml file is present
    if path_yaml.exists():
        with open(path_yaml, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                logging.error(e)
                coloredlogs.install(level=default_level)

    # Just use the normal configuration
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')

def as_list(obj, length=None, tp=None, iter_to_list=True):
    """
    Force an argument to be a list, optionally of a given length, optionally
    with all elements cast to a given type if not None.

    Parameters
    ---------
    obj : Object
        The obj we want to convert to a list.

    length : int or None, optional
        Length of new list. Applies if the inputted obj is not an iterable and
        iter_to_list is false.

    tp : type, optional
        Type to cast the values inside the list as.

    iter_to_list : bool, optional
        Determines if we should cast an iterable (not str) obj as a list or to
        enclose it in one.

    Returns
    -------
    obj : list
        The object enclosed or cast as a list.
    """
    # If the obj is None, return empty list or fixed-length list of Nones
    if obj is None:
        if length is None:
            return []
        return [None] * length
    
    # If it is already a list do nothing
    elif isinstance(obj, list):
        pass

    # If it is an iterable (and not str), convert it to a list
    elif isiterable(obj) and iter_to_list:
        obj = list(obj)
        
    # Otherwise, just enclose in a list making it the inputted length
    else:
        try:
            obj = [obj] * length
        except TypeError:
            obj = [obj]
        
    # Cast to type; Let exceptions here bubble up to the top.
    if tp is not None:
        obj = [tp(o) for o in obj]
    return obj

def isiterable(obj):
    """
    Function that determines if an object is an iterable, not including 
    str.

    Parameters
    ----------
    obj : object
        Object to test if it is an iterable.

    Returns
    -------
    bool : bool
        True if the obj is an iterable, False if not.
    """
    if isinstance(obj, str):
        return False
    else:
        return isinstance(obj, Iterable)

def _flatten(inp_iter):
    """
    Recursively iterate through values in nested iterables.

    Parameters
    ----------
    inp_iter : iterable
        The iterable to flatten.

    Returns
    -------
    value : object
        The contents of the iterable
    """
    for val in inp_iter:
        if isiterable(val):
            for ival in _flatten(val):
                yield ival
        else:
            yield val
            
def flatten(inp_iter):
    """
    Returns a flattened list of the inputted iterable.

    Parameters
    ----------
    inp_iter : iterable
        The iterable to flatten.

    Returns
    -------
    flattened_iter : list
        The contents of the iterable as a flat list
    """
    return list(_flatten(inp_iter))
