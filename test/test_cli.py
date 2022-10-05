import pytest  # type: ignore

import piemap.cli as cli


def test_main_ok_funny_arg():
    job = ['[]']
    assert cli.main(job) == 0


def test_main_ok_empty_array():
    job = []
    assert cli.main(job) == 0


def test_main_nok_wrong_type_int():
    bad = 42
    message = r"'int' object is not iterable"
    with pytest.raises(TypeError, match=message):
        cli.main(bad)  # type: ignore


def test_parse_request_empty():
    assert cli.parse_request([]) == 0


def test_parse_request_contradict(capsys):
    message = '2'
    with pytest.raises(SystemExit, match=message):
        cli.parse_request(['-q', '-v'])  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert 'you cannot be quiet and verbose at the same time' in err


def test_parse_request_invalid_format(capsys):
    message = '2'
    alien = 'alien'
    with pytest.raises(SystemExit, match=message):
        cli.parse_request(['-f', f'jpeg,png,{alien},svg'])  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert f'requested format {alien} for quality pie not in {cli.KNOWN_FORMATS}' in err


def test_parse_request_default_out(capsys):
    options = cli.parse_request(['-i', 'piemap.dsl'])  # type: ignore
    assert options.input_path == 'piemap.dsl'
    assert not options.verbose
    assert not options.quiet
    assert options.format_type_csl == 'png'
    assert options.out_path == 'piemap'


def test_parse_request_pos_in(capsys):
    options = cli.parse_request(['piemap.dsl'])  # type: ignore
    assert options.input_path == 'piemap.dsl'


def test_parse_request_default_dsl(capsys):
    options = cli.parse_request(['-o', 'bizarre'])  # type: ignore
    assert options.input_path == 'piemap.dsl'
    assert options.out_path == 'bizarre'
