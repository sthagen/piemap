# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.projections as pr


def test_min_from_limit_max_sample_one_ok():
    assert pr.min_from_limit_max(-1, 2) == -6


def test_min_from_limit_max_sample_two_ok():
    assert pr.min_from_limit_max(5, 8) == 0


def test_limit_folded_from_limit_max_sample_one_ok():
    assert pr.limit_folded_from_limit_max(-1, 2) == 5


def test_limit_folded_from_limit_max_sample_two_ok():
    assert pr.limit_folded_from_limit_max(5, 8) == 11


def test_min_folded_from_limit_max_sample_one_ok():
    assert pr.min_folded_from_limit_max(-1, 2) == 10


def test_min_folded_from_limit_max_sample_two_ok():
    assert pr.min_folded_from_limit_max(5, 8) == 16


def test_value_folded_from_limit_max_sample_one_ok():
    assert pr.value_folded_from_limit_max(-1, 2) == 5
