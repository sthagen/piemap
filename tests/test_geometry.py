# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.geometry as geom


def test_exact_top_of_center_true_ok():
    assert geom.exact_top_of_center(270) is True


def test_exact_top_of_center_false_ok():
    assert geom.exact_top_of_center(270 + 1) is False
