"""Create single view visualization mapping parameter values to an area scale resembling a (quality) pie."""
import argparse
from typing import no_type_check

from piemap import DEBUG, ENCODING, ENCODING_ERRORS_POLICY, log


@no_type_check
def parse(text):  # noqa
    """Later we parse the DSL."""
    return NotImplemented


def main(options: argparse.Namespace) -> int:
    log.info(f'{DEBUG=}, {ENCODING=}, {ENCODING_ERRORS_POLICY=}')
    return 0
