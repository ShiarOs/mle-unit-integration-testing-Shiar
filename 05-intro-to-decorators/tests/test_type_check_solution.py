"""Reference checks for the completed type_check implementation."""

from src.unit_test_examples.type_check_solution import type_check


# Matching return type: the decorated function should return the original result.
@type_check(int)
def times2(num):
    return num * 2


# Mismatching return type: the wrapper should print and return None.
@type_check(int)
def times2_bad_type(num):
    return str(num * 2)


def test_type_check_solution_returns_value_when_type_matches():
    assert times2(3) == 6


def test_type_check_solution_returns_none_for_wrong_type(capsys):
    assert times2_bad_type(3) is None
    assert capsys.readouterr().out.strip() == "Bad Type"
