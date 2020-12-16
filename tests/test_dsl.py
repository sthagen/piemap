# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.dsl as dsl


def test_dump_stub_ok():
    assert dsl.dump({}) is NotImplemented
