# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import hypothesis.strategies as st
from hypothesis import given

import piemap.dsl as dsl


def test_dumps_stub_ok():
    assert dsl.dumps({}) == '{}'


def test_loads_stub_ok():
    assert dsl.loads('') is NotImplemented


def test_is_numeric_true_ok():
    assert dsl.is_numeric('42') is True


def test_is_numeric_false_ok():
    assert dsl.is_numeric('fourtytwo') is False


def test_parse_empty():
    default_text_0 = ''

    default_generated_0 = [
        {
            'AXIS_INDEX': 0,
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
        },
    ]

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
        {
            'AXIS_INDEX': 1,
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
        'Index positions not ordered. Misplaced candidate is 1, found at 0',
        'Index positions not ordered. Misplaced candidate is 0, found at 1',
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
        'Conflicting index rules. Failing candidate is (333), reason is GT_NROW',
        'Index positions not ordered. Misplaced candidate is 333, found at 0',
        'Conflicting index rules. Failing candidate is (333), reason is GT_NROW',
        'Index positions not ordered. Misplaced candidate is 333, found at 1',
        'Conflicting index positions. Failing candidate/s is/are [333], reason is NONUNIQUE_INDEX',
    ]

    assert dsl.parse(default_text_2_collision) == (default_parsed_2_collision, default_diagnostics_2_collision)


def test_parse_d1f_ok():
    text = """\
    0;D1FX;FOLDED;;12;15;;;6;dB
    """

    ast = [
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

    diag = [' OK index (0) requested, accepted as (0)']

    assert dsl.parse(text) == (ast, diag)


def test_parse_d2f_ok():
    text = """\
    1;D2F;FOLDED;;12;15;;;12;V
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D2F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'V',
            'AXIS_VALUE': 12,
        },
    ]

    diag = [
        ' OK index (1) requested, accepted as (1)',
        'Conflicting index rules. Failing candidate is (1), reason is GT_NROW',
        'Index positions not ordered. Misplaced candidate is 1, found at 0',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_d3f_ok():
    text = """\
    2;D3F;FOLDED;;12;15;NULL;1
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D3F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        ' OK index (2) requested, accepted as (2)',
        'Conflicting index rules. Failing candidate is (2), reason is GT_NROW',
        'Index positions not ordered. Misplaced candidate is 2, found at 0',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_d4f_ok():
    text = """\
    ;D4F;FOLDED;;12;15;16;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D4F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d5f_ok():
    text = """\
    ;D5F;FOLDED;;12;15;18;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D5F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d6f_ok():
    text = """\
    ;D6F;FOLDED;;12;15;22;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D6F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d7b_ok():
    text = """\
    ;D7B;BIMONOTONE;0;80;100;;;40;%;SHOW_MIN
    """

    ast = [
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

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d7b_wrong_index_type_ok():
    wrong_index_type_text = """\
    WRONG;D7B;BIMONOTONE;0;80;100;;;40;%;SHOW_MIN
    """

    ast = [
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

    wrong_index_type_diag = [
        'NOK invalid index (WRONG) requested, accepted per parsing order as (0)',
        'Conflicting index rules. Failing candidate is (WRONG), reason is DC_INTEGER',
        'Index positions not ordered. Misplaced candidate is WRONG, found at 0',
    ]

    assert dsl.parse(wrong_index_type_text) == (ast, wrong_index_type_diag)


def test_parse_d8l_ok():
    text = """\
    ;D8L;;;1;2;;;0.5;#
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D8L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '#',
            'AXIS_VALUE': 0.5,
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d9f_ok():
    text = """\
    ;D9F;FOLDED;;12;15;;;12;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': 18,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 7,
            'AXIS_MIN_FOLDED': 23,
            'AXIS_NAME': 'D9F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 12,
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d10l_ok():
    text = """\
    ;D10L;;;1;2;;;0.25;ms
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 1,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 2,
            'AXIS_META': '',
            'AXIS_MIN': -0.6666666666666666,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D10L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 'ms',
            'AXIS_VALUE': 0.25,
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d11l_ok():
    text = """\
    ;D11L;;;2;1;;;0.8;kbit/s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 2,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 3.6666666666666665,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D11L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 'kbit/s',
            'AXIS_VALUE': 0.8,
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_d12l_ok():
    text = """\
    ;D12L;;;0.8;1;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_value_neither_null_nor_numeric_ok():
    text = """\
    ;D12L;;;0.8;1;;;wrong_value;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = []

    assert dsl.parse(text) == (ast, diag)


def test_parse_limit_not_numeric_ok():
    text = """\
    ;D12L;;;non_numeric_limit;1;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 'non_numeric_limit',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        'NOK limit(non_numeric_limit) and max(1) not both numeric, ignored linear axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_folded_limit_not_numeric_ok():
    text = """\
    ;D9F;FOLDED;;non_numeric_limit;15;;;12;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 'non_numeric_limit',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 15,
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D9F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 12,
        },
    ]

    diag = [
        'NOK limit(non_numeric_limit) and max(15) not both numeric, ignored folded axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_max_not_numeric_ok():
    text = """\
    ;D12L;;;0.8;non_numeric_max;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 'non_numeric_max',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        'NOK limit(0.8) and max(non_numeric_max) not both numeric, ignored linear axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_folded_max_not_numeric_ok():
    text = """\
    ;D9F;FOLDED;;12;non_numeric_max;;;12;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 12,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 'non_numeric_max',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D9F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 12,
        },
    ]

    diag = [
        'NOK limit(12) and max(non_numeric_max) not both numeric, ignored folded axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_limit_and_max_not_numeric_ok():
    text = """\
    ;D12L;;;non_numeric_limit;non_numeric_max;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 'non_numeric_limit',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 'non_numeric_max',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        'NOK limit(non_numeric_limit) and max(non_numeric_max) not both numeric, ignored linear axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_folded_limit_and_max_not_numeric_ok():
    text = """\
    ;D9F;FOLDED;;non_numeric_limit;non_numeric_max;;;12;dB
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 'non_numeric_limit',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 'non_numeric_max',  # This is maybe not what we want ... TODO(sthagen)
            'AXIS_META': '',
            'AXIS_MIN': 0.0,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D9F',
            'AXIS_TYPE': 'FOLDED',
            'AXIS_UNIT': 'dB',
            'AXIS_VALUE': 12,
        },
    ]

    diag = [
        'NOK limit(non_numeric_limit) and max(non_numeric_max) not both numeric, ignored folded axis at index (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_index_as_float_ok():
    text = """\
    0.333;D12L;;;0.8;1;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        'NOK invalid index (0.333) requested, accepted per parsing order as (0)',
        'Conflicting index rules. Failing candidate is (0.333), reason is DC_INTEGER',
        'Index positions not ordered. Misplaced candidate is 0.333, found at 0',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_index_negative_zero_ok():
    text = """\
    -0;D12L;;;0.8;1;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        ' OK index (0) requested, accepted as (0)',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_index_negative_wun_ok():
    text = """\
    -1;D12L;;;0.8;1;;;NULL;s
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'D12L',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': 's',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        ' OK index (-1) requested, accepted as (-1)',  # Maybe unwanted behavior TODO(sthagen)
        'Conflicting index rules. Failing candidate is (-1), reason is LT_ZERO',
        'Index positions not ordered. Misplaced candidate is -1, found at 0',
    ]

    assert dsl.parse(text) == (ast, diag)


def test_parse_too_many_axes_ok():
    text = """\
    ;A1;;;0.8;1;;;NULL;
    ;A2;;;0.8;1;;;NULL;
    ;A3;;;0.8;1;;;NULL;
    ;A4;;;0.8;1;;;NULL;
    ;A5;;;0.8;1;;;NULL;
    ;A6;;;0.8;1;;;NULL;
    ;A7;;;0.8;1;;;NULL;
    ;A8;;;0.8;1;;;NULL;
    ;A9;;;0.8;1;;;NULL;
    ;A10;;;0.8;1;;;NULL;
    ;A11;;;0.8;1;;;NULL;
    ;A12;;;0.8;1;;;NULL;
    ;A13;;;0.8;1;;;NULL;
    ;A14;;;0.8;1;;;NULL;
    ;A15;;;0.8;1;;;NULL;
    ;A16;;;0.8;1;;;NULL;
    ;A17_is_too_much;;;0.8;1;;;NULL;
    """

    ast = [
        {
            'AXIS_INDEX': 0,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A1',
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
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A2',
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
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A3',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 3,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A4',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 4,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A5',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 5,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A6',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 6,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A7',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 7,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A8',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 8,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A9',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 9,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A10',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 10,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A11',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 11,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A12',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 12,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A13',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 13,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A14',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 14,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A15',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
        {
            'AXIS_INDEX': 15,
            'AXIS_LIMIT': 0.8,
            'AXIS_LIMIT_FOLDED': False,
            'AXIS_MAX': 1,
            'AXIS_META': '',
            'AXIS_MIN': 0.4666666666666668,
            'AXIS_MIN_FOLDED': False,
            'AXIS_NAME': 'A16',
            'AXIS_TYPE': 'LINEAR',
            'AXIS_UNIT': '1',
            'AXIS_VALUE': 'NULL',
        },
    ]

    diag = [
        '17 dimensions requested, but only 16 accepted. Maximum is 16',
    ]

    assert dsl.parse(text) == (ast, diag)


@given(a_mi=st.floats(), a_li=st.floats(), a_ma=st.floats(), a_va=st.floats())
def test_parse_bimonotone_floats_stat(a_mi, a_li, a_ma, a_va):
    text = f"""\
    ;DXL;BIMONOTONE;{a_mi};{a_li};{a_ma};;;{a_va};%;SHOW_MIN
    """

    diag = []

    ([axis], diagnoses) = dsl.parse(text)
    assert axis['AXIS_INDEX'] == 0
    assert isinstance(axis['AXIS_LIMIT'], (float, int))
    assert axis['AXIS_LIMIT_FOLDED'] is False
    assert isinstance(axis['AXIS_MAX'], (float, int))
    assert axis['AXIS_META'] == 'SHOW_MIN'
    assert isinstance(axis['AXIS_MIN'], (float, int))
    assert axis['AXIS_MIN_FOLDED'] is False
    assert axis['AXIS_NAME'] == 'DXL'
    assert axis['AXIS_TYPE'] == 'BIMONOTONE'
    assert axis['AXIS_UNIT'] == '%'
    assert isinstance(axis['AXIS_VALUE'], (float, int))
    assert diagnoses == diag
