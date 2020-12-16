# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl

"""
SHOW_TITLE;A title for the plot
SHOW_VALUE;1
SHOW_MIN;0
"""
DEFAULT_TEXT = """\
0;D1F;FOLDED;;12;15;6;dB
1;D3F;FOLDED;;12;15;NULL;1
2;D2F;FOLDED;;12;15;12;V
;D4F;FOLDED;;12;15;16;dB
;D5F;FOLDED;;12;15;18;dB
;D6F;FOLDED;;12;15;22;dB
;D7B;BIMONOTONE;0;80;100;40;%;SHOW_MIN
;D8L;;;1;2;0.5;#
;D9F;FOLDED;;12;15;12;dB
;D10L;;;1;2;0.25;ms
;D11L;;;2;1;0.8;kbit/s
;D12L;;;0.8;1;NULL;s
;D13L;;;0.8;1;NULL;s
;D14L;;;0.8;1;NULL;s
;D15L;;;0.8;1;NULL;s
;D16L;;;0.8;1;NULL;s
"""

DEFAULT_PARSED = [
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
        'AXIS_VALUE': 'NULL'},
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
        'AXIS_VALUE': 'NULL'},
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
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 3,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 4,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 5,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 6,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 7,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 8,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 9,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 10,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 11,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 12,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 13,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 14,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'},
    {
        'AXIS_INDEX': 15,
        'AXIS_LIMIT': 0.8,
        'AXIS_LIMIT_FOLDED': False,
        'AXIS_MAX': 1.0,
        'AXIS_MIN': 0.4666666666666668,
        'AXIS_MIN_FOLDED': False,
        'AXIS_NAME': 'Dimension',
        'AXIS_TYPE': 'LINEAR',
        'AXIS_UNIT': '1',
        'AXIS_VALUE': 'NULL'}
]

#     '19 dimensions requested, but only 16 accepted. Maximum is 16',
DEFAULT_DIAGNOSTICS = [
    'Conflicting index rules. Failing IndexCand is 0, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 1, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 2, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 3, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 4, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 5, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 6, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 7, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 8, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 9, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 10, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 11, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 12, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 13, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 14, reason is DC_INTEGER',
    'Conflicting index rules. Failing IndexCand is 15, reason is DC_INTEGER'
]


def test_dumps_stub_ok():
    assert dsl.dumps({}) == "{}"


def test_loads_stub_ok():
    assert dsl.loads("") is NotImplemented


def test_parse_empty():
    assert dsl.parse('') == ([{'AXIS_INDEX': 0,
                               'AXIS_LIMIT': 0.8,
                               'AXIS_LIMIT_FOLDED': False,
                               'AXIS_MAX': 1.0,
                               'AXIS_MIN': 0.0,
                               'AXIS_MIN_FOLDED': False,
                               'AXIS_NAME': 'Dimension',
                               'AXIS_TYPE': 'LINEAR',
                               'AXIS_UNIT': '1',
                               'AXIS_VALUE': 'NULL'},
                              {'AXIS_INDEX': 1,
                               'AXIS_LIMIT': 0.8,
                               'AXIS_LIMIT_FOLDED': False,
                               'AXIS_MAX': 1.0,
                               'AXIS_MIN': 0.0,
                               'AXIS_MIN_FOLDED': False,
                               'AXIS_NAME': 'Dimension2',
                               'AXIS_TYPE': 'LINEAR',
                               'AXIS_UNIT': '1',
                               'AXIS_VALUE': 'NULL'},
                              {'AXIS_INDEX': 2,
                               'AXIS_LIMIT': 0.8,
                               'AXIS_LIMIT_FOLDED': False,
                               'AXIS_MAX': 1.0,
                               'AXIS_MIN': 0.0,
                               'AXIS_MIN_FOLDED': False,
                               'AXIS_NAME': 'DimensionFolded',
                               'AXIS_TYPE': 'FOLDED',
                               'AXIS_UNIT': 'dB',
                               'AXIS_VALUE': 'NULL'}],
                             ['Default used, since no input given.'])


def test_parse_default():
    assert dsl.parse(DEFAULT_TEXT) == (DEFAULT_PARSED, DEFAULT_DIAGNOSTICS)
