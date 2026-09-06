"""Decorator factory for validating the return type of a wrapped function."""

# @TODO Implementation Target (file-based):
# Objective: Implement a decorator that validates decorated function return types.
# Edit files:
# - src/unit_test_examples/type_check.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_type_check.py
# Solution:
# - src/unit_test_examples/type_check_solution.py


def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, correct_type):
                print("Bad Type")
                return None
            return result
        return wrapper
    return decorator
