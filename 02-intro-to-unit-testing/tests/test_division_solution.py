import pytest
from src.unit_test_examples.division import divide


# Reference solution: one parameterized test covers every divide case.
@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (3, 2, 1.5),
        (5, 5, 1),
        (6, 2, 3),
        (-2, 0, "Cannot divide by zero"),
        (10, -2, -5),
    ],
)
def test_divide_parametrized(x, y, expected_result):
    assert divide(x, y) == expected_result
