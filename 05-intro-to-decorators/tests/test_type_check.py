"""Validation checks for the type_check implementation target."""

from src.unit_test_examples.type_check import type_check


def test_type_check_returns_value_when_type_matches():
    @type_check(int)
    def times2(num):
        return num * 2

    assert times2(3) == 6


def test_type_check_returns_none_for_wrong_type(capsys):
    @type_check(int)
    def times2_bad_type(num):
        return str(num * 2)

    assert times2_bad_type(3) is None
    assert capsys.readouterr().out.strip() == "Bad Type"
