# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.projections as pr


def test_min_from_limit_max_sample_ok():
    assert pr.min_from_limit_max(-1, 2) == -6
