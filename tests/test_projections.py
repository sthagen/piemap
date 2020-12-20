# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
from hypothesis import given
import hypothesis.strategies as st
import pytest  # type: ignore

import piemap.projections as pr


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


def test_value_folded_from_limit_max_sample_one_ok():
    assert pr.value_folded_from_limit_max(-1, 2) == 5


def test_value_folded_from_limit_max_sample_two_ok():
    assert pr.value_folded_from_limit_max(5, 8) == 11


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
