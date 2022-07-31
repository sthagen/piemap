# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import hypothesis.strategies as st
from hypothesis import given

import piemap.projections as pr

ORDERED_SAMPLE_ONE = ('3', '2c', '2b', '2a', '1')
ORDERED_SAMPLE_TWO = ('ORIGIN', 'not ok', 'LIMIT_VALUE', 'ok')


def test_min_from_limit_max_sample_one_ok():
    assert pr.min_from_limit_max(-1, 2) == -6


def test_min_from_limit_max_sample_two_ok():
    assert pr.min_from_limit_max(5, 8) == 0


def test_min_from_limit_max_sample_d1f_ok():
    assert pr.min_from_limit_max(12, 15) == 7


def test_domain_from_limit_max_sample_one_ok():
    assert pr.domain_from_limit_max(-1, 2) == (-6, 2)


def test_limit_folded_from_limit_max_sample_one_ok():
    assert pr.limit_folded_from_limit_max(-1, 2) == 5


def test_limit_folded_from_limit_max_sample_two_ok():
    assert pr.limit_folded_from_limit_max(5, 8) == 11


def test_min_folded_from_limit_max_sample_one_ok():
    assert pr.min_folded_from_limit_max(-1, 2) == 10


def test_min_folded_from_limit_max_sample_two_ok():
    assert pr.min_folded_from_limit_max(5, 8) == 16


def test_min_folded_from_limit_max_sample_d1f_ok():
    assert pr.min_folded_from_limit_max(12, 15) == 23


def test_domain_folded_from_limit_max_sample_one_ok():
    assert pr.domain_folded_from_limit_max(-1, 2) == (-6, 10)


def test_domain_folded_from_limit_max_sample_two_ok():
    assert pr.domain_folded_from_limit_max(5, 8) == (0, 16)


def test_domain_folded_from_limit_max_sample_d1f_ok():
    assert pr.domain_folded_from_limit_max(12, 15) == (7, 23)


def test_value_folded_from_limit_max_sample_one_ok():
    assert pr.value_folded_from_limit_max(-1, 2) == 5


def test_value_folded_from_limit_max_sample_two_ok():
    assert pr.value_folded_from_limit_max(5, 8) == 11


def test_limit_ordered_from_domain_sample_one_ok():
    assert pr.limit_ordered_from_domain(ORDERED_SAMPLE_ONE) == '2b'


def test_limit_ordered_from_domain_sample_two_ok():
    assert pr.limit_ordered_from_domain(ORDERED_SAMPLE_TWO) == 'LIMIT_VALUE'


def test_min_ordered_from_domain_sample_one_ok():
    assert pr.min_ordered_from_domain(ORDERED_SAMPLE_ONE) == ORDERED_SAMPLE_ONE[0]


def test_limit_ordered_from_domain_with_limit_value_ok():
    assert pr.limit_ordered_from_domain(('LIMIT_VALUE', 42, False, {})) == 'LIMIT_VALUE'


def test_limit_ordered_from_domain_empty_ok():
    assert pr.limit_ordered_from_domain([]) == 'NULL'


def test_limit_ordered_from_domain_even_ok():
    assert pr.limit_ordered_from_domain([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 1


def test_limit_ordered_from_domain_odd_ok():
    assert pr.limit_ordered_from_domain([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1


def test_limit_ordered_from_domain_minimal_even_ok():
    assert pr.limit_ordered_from_domain([0, 0, 1, 0]) == 1


def test_limit_ordered_from_domain_minimal_odd_ok():
    assert pr.limit_ordered_from_domain([0, 1, 0]) == 1


def test_min_ordered_from_domain_sample_two_ok():
    assert pr.min_ordered_from_domain(ORDERED_SAMPLE_TWO) == ORDERED_SAMPLE_TWO[0]


def test_min_ordered_from_domain_empty_ok():
    assert pr.min_ordered_from_domain([]) == 'NULL'


def test_domain_ordered_from_domain_sample_one_ok():
    assert pr.domain_ordered_from_domain(ORDERED_SAMPLE_ONE) == ORDERED_SAMPLE_ONE


def test_domain_ordered_from_domain_sample_two_ok():
    assert pr.domain_ordered_from_domain(ORDERED_SAMPLE_TWO) == ORDERED_SAMPLE_TWO


def test_domain_ordered_from_domain_empty_ok():
    assert pr.domain_ordered_from_domain([]) == 'NULL'


def test_max_ordered_from_domain_sample_one_ok():
    assert pr.max_ordered_from_domain(ORDERED_SAMPLE_ONE) == ORDERED_SAMPLE_ONE[-1]


def test_max_ordered_from_domain_sample_two_ok():
    assert pr.max_ordered_from_domain(ORDERED_SAMPLE_TWO) == ORDERED_SAMPLE_TWO[-1]


def test_max_ordered_from_domain_empty_ok():
    assert pr.max_ordered_from_domain([]) == 'NULL'


@given(limit=st.integers(), maximum=st.integers())
def test_min_from_limit_max_int_int(limit, maximum):
    minimum = pr.min_from_limit_max(limit, maximum)
    assert isinstance(minimum, (float, int))


@given(limit=st.floats(), maximum=st.integers())
def test_min_from_limit_max_float_int(limit, maximum):
    minimum = pr.min_from_limit_max(limit, maximum)
    assert isinstance(minimum, (float, int))


@given(limit=st.integers(), maximum=st.floats())
def test_min_from_limit_max_int_float(limit, maximum):
    minimum = pr.min_from_limit_max(limit, maximum)
    assert isinstance(minimum, (float, int))


@given(limit=st.floats(), maximum=st.floats())
def test_min_from_limit_max_float_float(limit, maximum):
    minimum = pr.min_from_limit_max(limit, maximum)
    assert isinstance(minimum, (float, int))


@given(limit=st.integers(), maximum=st.integers())
def test_limit_folded_from_limit_max_int_int(limit, maximum):
    limit_folded = pr.limit_folded_from_limit_max(limit, maximum)
    assert isinstance(limit_folded, (float, int))


@given(limit=st.floats(), maximum=st.integers())
def test_limit_folded_from_limit_max_float_int(limit, maximum):
    limit_folded = pr.limit_folded_from_limit_max(limit, maximum)
    assert isinstance(limit_folded, (float, int))


@given(limit=st.integers(), maximum=st.floats())
def test_limit_folded_from_limit_max_int_float(limit, maximum):
    limit_folded = pr.limit_folded_from_limit_max(limit, maximum)
    assert isinstance(limit_folded, (float, int))


@given(limit=st.floats(), maximum=st.floats())
def test_limit_folded_from_limit_max_float_float(limit, maximum):
    limit_folded = pr.limit_folded_from_limit_max(limit, maximum)
    assert isinstance(limit_folded, (float, int))


@given(limit=st.integers(), maximum=st.integers())
def test_min_folded_from_limit_max_int_int(limit, maximum):
    minimum_folded = pr.min_folded_from_limit_max(limit, maximum)
    assert isinstance(minimum_folded, (float, int))


@given(limit=st.floats(), maximum=st.integers())
def test_min_folded_from_limit_max_float_int(limit, maximum):
    minimum_folded = pr.min_folded_from_limit_max(limit, maximum)
    assert isinstance(minimum_folded, (float, int))


@given(limit=st.integers(), maximum=st.floats())
def test_min_folded_from_limit_max_int_float(limit, maximum):
    minimum_folded = pr.min_folded_from_limit_max(limit, maximum)
    assert isinstance(minimum_folded, (float, int))


@given(limit=st.floats(), maximum=st.floats())
def test_min_folded_from_limit_max_float_float(limit, maximum):
    minimum_folded = pr.min_folded_from_limit_max(limit, maximum)
    assert isinstance(minimum_folded, (float, int))


@given(limit=st.integers(), maximum=st.integers())
def test_value_folded_from_limit_max_int_int(limit, maximum):
    value = pr.value_folded_from_limit_max(limit, maximum)
    assert isinstance(value, (float, int))


@given(limit=st.floats(), maximum=st.integers())
def test_value_folded_from_limit_max_float_int(limit, maximum):
    value = pr.value_folded_from_limit_max(limit, maximum)
    assert isinstance(value, (float, int))


@given(limit=st.integers(), maximum=st.floats())
def test_value_folded_from_limit_max_int_float(limit, maximum):
    value = pr.value_folded_from_limit_max(limit, maximum)
    assert isinstance(value, (float, int))


@given(limit=st.floats(), maximum=st.floats())
def test_value_folded_from_limit_max_float_float(limit, maximum):
    value = pr.value_folded_from_limit_max(limit, maximum)
    assert isinstance(value, (float, int))
