# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl

DEFAULT_TEXT_0 = ''

DEFAULT_GENERATED_0 = [
    {'AXIS_INDEX': 0,
     'AXIS_LIMIT': 0.8,
     'AXIS_LIMIT_FOLDED': False,
     'AXIS_MAX': 1.0,
     'AXIS_MIN': 0.0,
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
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.0,
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
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.0,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'DimensionFolded',
        'AXIS_TYPE': 'FOLDED',
        'AXIS_UNIT': 'dB',
        'AXIS_VALUE': 'NULL',
    },
]

DEFAULT_DIAGNOSTICS_0 = ['Default used, since no input given.']

DEFAULT_TEXT_1 = """\
0;D1F;FOLDED;;12;15;6;dB
"""

DEFAULT_PARSED_1 = [
    {
        'AXIS_INDEX': 0,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL',
    },
]

DEFAULT_DIAGNOSTICS_1 = []

DEFAULT_TEXT_2 = """\
;L 0;;;1;2;NULL;
;L 1;;;1;2;-0.1;
"""

DEFAULT_PARSED_2 = [
    {'AXIS_INDEX': 0,
     'AXIS_LIMIT': 0.8,
     'AXIS_LIMIT_FOLDED': False,
     'AXIS_MAX': 1.0,
     'AXIS_MIN': 0.4666666666666668,
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
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL',
    },
]

DEFAULT_DIAGNOSTICS_2 = []

DEFAULT_TEXT_3 = """\
;F 1;FOLDED;;1;2;2;
;F 2;FOLDED;;1;2;0;
;F 3;FOLDED;;1;2;0.25;
"""

DEFAULT_PARSED_3 = [
    {
        'AXIS_INDEX': 0,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
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
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL',
    },
    {
        'AXIS_INDEX': 2,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL',
    },
]

DEFAULT_DIAGNOSTICS_3 = []


def test_dumps_stub_ok():
    assert dsl.dumps({}) == "{}"


def test_loads_stub_ok():
    assert dsl.loads("") is NotImplemented


def test_is_numeric_true_ok():
    assert dsl.is_numeric('42') is True


def test_is_numeric_false_ok():
    assert dsl.is_numeric('fourtytwo') is False


def test_parse_empty():
    assert dsl.parse(DEFAULT_TEXT_0) == (DEFAULT_GENERATED_0, DEFAULT_DIAGNOSTICS_0)


def test_parse_dim_one_linear():
    assert dsl.parse(DEFAULT_TEXT_1) == (DEFAULT_PARSED_1, DEFAULT_DIAGNOSTICS_1)


def test_parse_dim_two_linear():
    assert dsl.parse(DEFAULT_TEXT_2) == (DEFAULT_PARSED_2, DEFAULT_DIAGNOSTICS_2)


def test_parse_dim_three_folded():
    assert dsl.parse(DEFAULT_TEXT_3) == (DEFAULT_PARSED_3, DEFAULT_DIAGNOSTICS_3)
