import hypothesis.strategies as st
from hypothesis import given

import piemap.bitmap as bitm


def test_start_of():
    assert bitm.start_of(0, 1) == (270 - 360 / 1 / 2) % 360


def test_middle_of():
    assert bitm.middle_of(0, 1) == 270


def test_end_of():
    assert bitm.end_of(0, 1) == (270 + 360 / 1 / 2) % 360


@given(n=st.integers(min_value=0, max_value=100))
def test_start_of_data_driven(n):
    n_max = n + 1
    assert 0 <= bitm.start_of(n, n_max) <= 360
