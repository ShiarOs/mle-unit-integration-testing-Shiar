"""Simple packaging example used by notebook exercises."""

# @TODO Exercise (file-based):
# Objective: Implement a tiny package function and import it from a notebook.
# Edit files:
# - src/example/example_file.py
# Validate with:
# - ../.venv/bin/python -c "from src.example.example_file import add_one; assert add_one(3) == 4"
# Solution:
# - src/example/example_file_solution.py


def add_one(number):
    return number + 1
