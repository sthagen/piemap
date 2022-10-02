# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import piemap.cli as cli


def test_main_ok_empty_array():
    job = ['[]']
    assert cli.main(job) == 0


def test_main_nok_wrong_type_intng():
    bad = 42
    message = r"'int' object is not iterable"
    with pytest.raises(TypeError, match=message):
        cli.main(bad)  # type: ignore
