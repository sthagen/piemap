#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Add logical documentation here later TODO."""
import os
import sys

DEBUG = bool(os.getenv('PIEMAP_DEBUG', ''))


def main(argv=None):
    """Process ... TODO."""
    argv = sys.argv[1:] if argv is None else argv
    verbose = True if '-v' in argv or '--verbose' in argv else False
    if verbose:
        print('Not yet implemented')
        if DEBUG:
            print(f'Arguments received: ({argv})')
