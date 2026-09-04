"""Normalize text and check whether it reads the same backwards."""

# @TODO Exercise (file-based):
# Objective: Implement palindrome normalization and symmetry check.
# Edit files:
# - src/unit_test_examples/palindrome.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_is_palindrome.py
# Solution:
# - src/unit_test_examples/palindrome_solution.py


def is_palindrome(s):
    # Work step by step so the test failures tell you which assumption broke.
    # 1) Normalize to lowercase.
    # 2) Remove spaces and punctuation.
    # 3) Compare normalized string with its reverse.
    #raise NotImplementedError("Implement is_palindrome in palindrome.py")
    normalized = s.lower()
    import string
    import re
    normalized = re.sub(r"[^A-Za-z0-9]+", "", normalized)
    return normalized == normalized[::-1]
    
