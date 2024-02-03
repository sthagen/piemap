"""One-view visualization of grouped characterizations (Quality Pie)."""

import datetime as dti
import logging
import os
import pathlib
from typing import no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.ed38dfeb'
# [[[end]]] (checksum: db573b62f771dae6170699431794e7d5)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: list[str] = [
    'ANGLE_MAX',
    'ANGLE_OFF',
    'CIRCLE_CENTER',
    'DARKRED',
    'DEBUG',
    'ENCODING',
    'ENCODING_ERRORS_POLICY',
    'GRAY',
    'GREEN',
    'HEIGHT',
    'HEIGHT_HALF',
    'HEIGHT_OFF',
    'LABEL_SIZE',
    'LINE_WIDTH',
    'PIE_BOX',
    'RADIUS',
    'RADIUS_HALF',
    'RED',
    'SUBTITLE_SIZE',
    'TITLE_SIZE',
    'TOP_LEFT_X',
    'TOP_LEFT_Y',
    'WHITE',
    'WIDTH',
    'WIDTH_HALF',
    'WIDTH_OFF',
    'YELLOW',
    'YELLOWGREEN',
    'log',
]

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

COLON = ':'
COMMA = ','
DEFAULT_LF_ONLY = 'YES'
DOT = '.'
KNOWN_FORMATS = ('jpeg', 'png', 'svg')
PIPE = '|'
SEMI = ';'

log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'

WIDTH = 1080
HEIGHT = WIDTH
DIAMETER = 900
WIDTH_HALF = WIDTH / 2
HEIGHT_HALF = HEIGHT / 2
RADIUS = DIAMETER / 2
WIDTH_OFF = 0
HEIGHT_OFF = 50
TOP_LEFT_X = WIDTH_HALF - RADIUS
TOP_LEFT_Y = HEIGHT_HALF - RADIUS + HEIGHT_OFF
PIE_BOX = ((TOP_LEFT_X, TOP_LEFT_Y), (TOP_LEFT_X + DIAMETER, TOP_LEFT_Y + DIAMETER))
CIRCLE_CENTER = (WIDTH_HALF, HEIGHT_HALF + HEIGHT_OFF)

ANGLE_OFF = 270
ANGLE_MAX = 360

# font sizes and line width
TITLE_SIZE = 40
SUBTITLE_SIZE = 24
LABEL_SIZE = 16
LINE_WIDTH = 1

# colors
DARKRED = '#900000'
GRAY = '#c0c0c0'
GREEN = '#008800'
RED = '#dd0000'
WHITE = '#ffffff'
YELLOW = '#ffff20'
YELLOWGREEN = '#77ff20'


def parse_csl(csl: str) -> list[str]:
    """DRY."""
    return [fmt.strip().lower() for fmt in csl.split(COMMA) if fmt.strip()]


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):  # noqa
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()  # pragma: no cover


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
