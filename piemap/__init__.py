"""One-view visualization of grouped characterizations (Quality Pie)."""
import os
from typing import List

APP_NAME = 'One-view visualization of grouped characterizations (Quality Pie).'
APP_ALIAS = 'piemap'
APP_ENV = 'PIEMAP'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.piemap.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.7.30+parent.d88d6233'
# [[[end]]] (checksum: 676141ef3144a8ea6ce2493608afe68f)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
