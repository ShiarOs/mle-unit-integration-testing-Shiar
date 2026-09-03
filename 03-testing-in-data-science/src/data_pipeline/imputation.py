import pandas as pd

# @TODO Exercise (file-based):
# Objective: Extend mean imputation with min/max variants and matching tests.
# Edit files:
# - src/data_pipeline/imputation.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_imputation.py
# Solution:
# - src/data_pipeline/imputation_solution.py


def impute(series: pd.Series) -> pd.Series:
    # This baseline mean-imputation helper already works; add sibling helpers by analogy.
    mean_val = series.mean()
    return series.fillna(mean_val)
