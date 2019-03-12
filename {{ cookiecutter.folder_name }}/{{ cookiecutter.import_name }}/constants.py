"""
Constants used throughout the repo.
"""
from pathlib import Path

# Define some Path objects to folders within the repo
DIR_REPO = Path(__file__).resolve().parent.parent
DIR_DATA = DIR_REPO / 'data'
DIR_DATA_EXT = DIR_DATA / 'external'
DIR_DATA_INT = DIR_DATA / 'interim'
DIR_DATA_PROC = DIR_DATA / 'processed'
DIR_DATA_RAW = DIR_DATA / 'raw'
DIR_FIG = DIR_REPO / 'figures'
DIR_FIG_FINAL = DIR_FIG / 'finalized'
DIR_FIG_UNSORTED = DIR_FIG / 'unsorted'
DIR_LOGS = DIR_REPO / 'logs'
DIR_NOTEBOOKS = DIR_REPO / 'notebooks'
DIR_MODELS = DIR_REPO / 'models'
DIR_REPORTS = DIR_REPO / 'reports'
DIR_REFERENCES = DIR_REPO / 'references'
