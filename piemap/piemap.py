# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Create single view visualization mapping parameter values to an area scale resembling a (quality) pie."""
import os

DEBUG_VAR = 'PIEMAP_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


def parse(text):
    """Later we parse the DSL."""
    return NotImplemented
