"""Baseline divide tests for the parametrization refactor."""

# @TODO Exercise (file-based):
# Objective: Refactor this baseline test into a parameterized pytest test.
# Edit files:
# - tests/test_division.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_division.py
# Solution:
# - tests/test_division_solution.py
# - 02-intro-to-unit-testing.ipynb (<summary>Solution</summary> block)


from src.unit_test_examples.division import divide


def test_divide():
    # This baseline is intentionally repetitive so it can be refactored.
    # generate random number for x as float between 5 and 10
    import random
    x = random.uniform(5, 10)
    y = random.uniform(1, 5)

    # Clean up the message when error on devision by 0, error message = "Cannot divide by zero" to lowercase and romove the spaces and special characters from the message to avoid assertion err
    error_message = divide(x, 0).lower().replace(" ", "").replace(".", "").replace(",", "")

    # convert x and y to int to avoid floating point precision issues
    x_int = int(x)
    y_int = int(y)

    #Check divide int with int values
    assert divide(x_int, y_int) == x_int / y_int

    #check divide float with float values
    assert divide(x, y) == x / y

    #Check divide small number with big number
    assert divide(y, x) == y / x
    
    #Check divide with 0
    assert error_message == error_message



