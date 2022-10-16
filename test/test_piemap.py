# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import piemap.api as pie


def test_parse_ok_empty_string():
    assert pie.parse('') is NotImplemented
