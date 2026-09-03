"""Regression tests for the baseline mean imputation helper."""

import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_series_equal
from src.data_pipeline.imputation import impute


@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 2.0, 3.0])),
        (pd.Series([1, 2, 3, np.nan, 4, np.nan]), pd.Series([1, 2, 3, 2.5, 4, 2.5])),
    ],
)
def test_impute(input_series, expected_result):
    # assert_series_equal checks both the values and the pandas Series structure.
    assert_series_equal(impute(input_series), expected_result)
