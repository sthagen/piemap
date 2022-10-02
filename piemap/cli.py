"""CLI interface for single view visualization mapping parameter values to an area scale resembling a (quality) pie."""
import argparse
import sys

import piemap.piemap as api
from piemap import APP_ALIAS, APP_NAME, KNOWN_FORMATS, parse_csl


def parse_request(argv: list[str]) -> int | argparse.Namespace:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--input-path',
        '-i',
        dest='input_path',
        default='',
        help='the data (format DSL) to create the quality pie. Optional\n(default: positional input path value)',
        required=False,
    )
    parser.add_argument(
        'input_path_pos',
        nargs='?',
        default='',
        help='path to data file.',
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default='piemap.png',
        help='output file path for graphic (default: piemap.png)',
    )
    parser.add_argument(
        '--formats',
        '-f',
        dest='format_type_csl',
        default='png',
        help='formats (jpeg, png, svg) as comma separated list for taxonomy (default: png)',
    )
    parser.add_argument(
        '--dry-run',
        '-d',
        dest='dry_run',
        default=False,
        action='store_true',
        help='only log what would be done - no real actions (default: False)',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        dest='quiet',
        default=False,
        action='store_true',
        help='work as quiet as possible (default: False)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way (default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.verbose and options.quiet:
        parser.error('you cannot be quiet and verbose at the same time')

    format_types = parse_csl(options.format_type_csl)
    for fmt in format_types:
        if fmt not in KNOWN_FORMATS:
            parser.error(f'requested format {fmt} for quality pie not in {KNOWN_FORMATS}')

    if not options.input_path:
        if options.input_path_pos:
            options.input_path = options.input_path_pos
        else:
            options.input_path = 'piemap.png'

    return options


def main(argv: list[str] | None = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.main(options)
