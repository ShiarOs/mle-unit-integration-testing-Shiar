"""Regression tests for the palindrome implementation target."""

import pytest
from src.unit_test_examples.palindrome import is_palindrome


@pytest.mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        # Cover empty input, normalization, and clear non-palindrome cases.
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
