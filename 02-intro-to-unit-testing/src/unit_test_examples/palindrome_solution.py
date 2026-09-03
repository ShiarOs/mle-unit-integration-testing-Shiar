"""Reference solution for the palindrome normalization exercise."""

import re


def is_palindrome(s):
    """Normalizes a string by converting it to lowercase and removing
    all non-alphanumeric characters. Then compares it to its reverse."""
    normalized = s.lower()
    normalized = re.sub(r"[^A-Za-z0-9]+", "", normalized)
    return normalized == normalized[::-1]
