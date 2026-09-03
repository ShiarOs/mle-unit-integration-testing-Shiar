"""Reference tests for the completed imputation helpers."""

import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_series_equal
from src.data_pipeline.imputation_solution import impute_max, impute_mean, impute_min


# Mean imputation should replace NaN with the arithmetic average.
@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 2.0, 3.0])),
        (pd.Series([1.0, 2.0, 3.0]), pd.Series([1.0, 2.0, 3.0])),
    ],
)
def test_impute_mean(input_series, expected_result):
    assert_series_equal(impute_mean(input_series), expected_result)


# Min imputation should replace NaN with the smallest observed value.
@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 1.0, 3.0])),
        (pd.Series([5.0, 2.0, 9.0]), pd.Series([5.0, 2.0, 9.0])),
    ],
)
def test_impute_min(input_series, expected_result):
    assert_series_equal(impute_min(input_series), expected_result)


# Max imputation should replace NaN with the largest observed value.
@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 3.0, 3.0])),
        (pd.Series([5.0, 2.0, 9.0]), pd.Series([5.0, 2.0, 9.0])),
    ],
)
def test_impute_max(input_series, expected_result):
    assert_series_equal(impute_max(input_series), expected_result)
