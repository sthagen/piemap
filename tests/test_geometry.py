# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.geometry as geom


def test_exact_top_of_center_true_ok():
    assert geom.exact_top_of_center(270) is True


def test_exact_top_of_center_false_ok():
    assert geom.exact_top_of_center(270 + 1) is False


def test_exact_bottom_of_center_true_ok():
    assert geom.exact_bottom_of_center(90) is True


def test_exact_bottom_of_center_false_ok():
    assert geom.exact_bottom_of_center(90 + 1) is False


def test_right_bottom_of_center_true_ok():
    assert geom.right_bottom_of_center(90 - 1) is True


def test_right_bottom_of_center_false_ok():
    assert geom.right_bottom_of_center(90) is False


def test_right_top_of_center_true_ok():
    assert geom.right_top_of_center(270 + 1) is True


def test_right_top_of_center_false_ok():
    assert geom.right_top_of_center(270) is False
