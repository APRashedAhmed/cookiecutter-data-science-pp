"""Constants used throughout the repo."""
from pathlib import Path

# Define some Path objects to folders within the repo
# Path to the repo as a whole
DIR_REPO = Path(__file__).resolve().parent.parent

# Path to the top-level data directories which contain the data
DIR_DATA = DIR_REPO / 'data'
DIR_DATA_EXT = DIR_DATA / 'external'
DIR_DATA_INT = DIR_DATA / 'interim'
DIR_DATA_PROC = DIR_DATA / 'processed'
DIR_DATA_RAW = DIR_DATA / 'raw'

# Path to the figures
DIR_FIG = DIR_REPO / 'figures'
DIR_FIG_FIN = DIR_FIG / 'finalized'
DIR_FIG_UNS = DIR_FIG / 'unsorted'

# Path to the log file directory
DIR_LOGS = DIR_REPO / 'logs'

# Path to the symbolically linked notebook and report directories
DIR_NBS_SL = DIR_REPO / 'notebooks'
DIR_RPS_SL = DIR_REPO / 'reports'

# Path to the models and checkpoint direcotories
DIR_MODELS = DIR_REPO / 'models'
DIR_CKPTS = DIR_MODELS / 'checkpoints'

# Path to paper references 
DIR_REFERENCES = DIR_REPO / 'references'

# Path to various locations within the documentation
DIR_DOCS = DIR_REPO / 'docs'
DIR_DOCS_SRC = DIR_DOCS / 'source'
DIR_NBS = DIR_DOCS_SRC / 'notebooks'
DIR_IMGS = DIR_DOCS_SRC / 'images'
DIR_RPS = DIR_DOCS_SRC / 'reports'
