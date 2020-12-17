# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl


def test_dumps_stub_ok():
    assert dsl.dumps({}) == "{}"


def test_loads_stub_ok():
    assert dsl.loads("") is NotImplemented


def test_is_numeric_true_ok():
    assert dsl.is_numeric('42') is True


def test_is_numeric_false_ok():
    assert dsl.is_numeric('fourtytwo') is False


def test_parse_empty():
    default_text_0 = ''

    default_generated_0 = [
        {'AXIS_INDEX': 0,
         'AXIS_LIMIT': 0.8,
         'AXIS_LIMIT_FOLDED': False,
         'AXIS_MAX': 1,
         'AXIS_META': '',
         'AXIS_MIN': 0,
         'AXIS_MIN_FOLDED': False,
         'AXIS_NAME': 'Dimension',
         'AXIS_TYPE': 'LINEAR',
         'AXIS_UNIT': '1',
         'AXIS_VALUE': 'NULL',
         },
        {
            'AXIS_INDEX': 1,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'Dimension2',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 2,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'DimensionFolded',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    default_diagnostics_0 = ['Default used, since no input given.']

    assert dsl.parse(default_text_0) == (default_generated_0, default_diagnostics_0)


def test_parse_dim_one_linear():
    default_text_1 = """\
    0;D1F;FOLDED;;12;15;6;dB
    """

    default_parsed_1 = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D1F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    default_diagnostics_1 = [' OK index (0) requested, accepted as (0)']

    assert dsl.parse(default_text_1) == (default_parsed_1, default_diagnostics_1)


def test_parse_dim_two_linear():
    default_text_2 = """\
    ;L 0;;;1;2;;;NULL;
    ;L 1;;;1;2;;;-0.1;
    """

    default_parsed_2 = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'L 0',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 1,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'L 1',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': -0.1,
        },
    ]

    default_diagnostics_2 = []

    assert dsl.parse(default_text_2) == (default_parsed_2, default_diagnostics_2)


def test_parse_dim_three_folded():
    default_text_3 = """\
    ;F 1;FOLDED;;1;2;;;2;
    ;F 2;FOLDED;;1;2;;;0;
    ;F 3;FOLDED;;1;2;;;0.25;
    """

    default_parsed_3 = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': 3,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': 4.666666666666667,
            'AXIS_NAME': 'F 1',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 2,
        },
        {
            'AXIS_INDEX': 1,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': 3,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': 4.666666666666667,
            'AXIS_NAME': 'F 2',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 0,
        },
        {
            'AXIS_INDEX': 2,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': 3,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': 4.666666666666667,
            'AXIS_NAME': 'F 3',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 0.25,
        }, ]

    default_diagnostics_3 = []

    assert dsl.parse(default_text_3) == (default_parsed_3, default_diagnostics_3)


def test_parse_dim_two_linear_unordered():
    default_text_2_unordered = """\
    1;L 0;;;1;2;;;NULL;
    0;L 1;;;1;2;;;-0.1;
    """

    default_parsed_2_unordered = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'L 1',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': -0.1,
        },
        {'AXIS_INDEX': 1,
         'AXIS_LIMIT': 1,
         'AXIS_LIMIT_FOLDED': False,
         'AXIS_MAX': 2,
         'AXIS_META': '',
         'AXIS_MIN': -0.6666666666666666,
         'AXIS_MIN_FOLDED': False,
         'AXIS_NAME': 'L 0',
         'AXIS_TYPE': 'LINEAR',
         'AXIS_UNIT': '1',
         'AXIS_VALUE': 'NULL',
         },
    ]

    default_diagnostics_2_unordered = [
        ' OK index (1) requested, accepted as (1)',
        ' OK index (0) requested, accepted as (0)',
        'Index positions not ordered. Misplaced IndexCand is 1, found at 0',
        'Index positions not ordered. Misplaced IndexCand is 0, found at 1',
    ]

    assert dsl.parse(default_text_2_unordered) == (default_parsed_2_unordered, default_diagnostics_2_unordered)


def test_parse_dim_two_linear_collision():
    default_text_2_collision = """\
    333;L 0C;;;1;2;;;NULL;
    333;L 1C;;;1;2;;;-0.1;;
    """

    default_parsed_2_collision = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'L 0C',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 1,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'L 1C',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': -0.1,
        },
    ]

    default_diagnostics_2_collision = [
        ' OK index (333) requested, accepted as (333)',
        ' OK index (333) requested, accepted as (333)',
        'Conflicting index rules. Failing IndexCand is 333, reason is GT_NROW',
        'Index positions not ordered. Misplaced IndexCand is 333, found at 0',
        'Conflicting index rules. Failing IndexCand is 333, reason is GT_NROW',
        'Index positions not ordered. Misplaced IndexCand is 333, found at 1',
        'Conflicting index positions. Failing IndexCand/s is/are [333], reason is NONUNIQUE_INDEX',
    ]

    assert dsl.parse(default_text_2_collision) == (default_parsed_2_collision, default_diagnostics_2_collision)


def test_parse_d1f_ok():
    d1f_text = """\
    0;D1FX;FOLDED;;12;15;;;6;dB
    """

    d1f_ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D1FX',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 6,
        },
    ]

    d1f_diag = [' OK index (0) requested, accepted as (0)']

    assert dsl.parse(d1f_text) == (d1f_ast, d1f_diag)


def test_parse_d7b_ok():
    d7b_text = """\
    ;D7B;BIMONOTONE;0;80;100;;;40;%;SHOW_MIN
    """

    d7b_ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 80,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 100,
            'AXIS_META': 'SHOW_MIN',
            'AXIS_MIN': 0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D7B',
            'AXIS_TYPE': 'BIMONOTONE',
            'AXIS_UNIT': '%',
            'AXIS_VALUE': 40,
        },
    ]

    d7b_diag = []

    assert dsl.parse(d7b_text) == (d7b_ast, d7b_diag)
