# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl


def test_dumps_stub_ok():
    assert dsl.dumps({}) is NotImplemented


def test_loads_stub_ok():
    assert dsl.loads("") is NotImplemented
