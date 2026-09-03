"""Regression tests for the transformation implementation targets."""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal, assert_series_equal
from src.data_pipeline.transformation import (
    get_sum_score_by_brand_and_gender,
    is_greater_than_average,
)


@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1, 2, 3, 2.5, 4]), pd.Series([0, 0, 1, 0, 1])),
        (pd.Series([10, 10, 10, 10]), pd.Series([0, 0, 0, 0])),
    ],
)
def test_is_greater_than_average(input_series, expected_result):
    # This check stays at the Series level: one output flag per input row.
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_result)
    assert isinstance(output_series, pd.Series)


@pytest.mark.parametrize(
    "input_frame, expected_result",
    [
        (
            pd.DataFrame(
                {
                    "brand": [
                        "Abercrombie",
                        "Abercrombie",
                        "Abercrombie",
                        "Abercrombie",
                    ],
                    "menWomen": ["men", "men", "women", "women"],
                    "size_greater_than_average": [1, 1, 0, 1],
                }
            ),
            pd.DataFrame(
                {
                    "brand": ["Abercrombie", "Abercrombie"],
                    "menWomen": ["men", "women"],
                    "size_greater_than_average": [2, 1],
                }
            ),
        ),
        (
            pd.DataFrame(
                {
                    "brand": [
                        "Abercrombie",
                        "Calvin Klein",
                        "Abercrombie",
                        "Abercrombie",
                    ],
                    "menWomen": ["men", "men", "women", "women"],
                    "size_greater_than_average": [1, 1, 0, 0],
                }
            ),
            pd.DataFrame(
                {
                    "brand": ["Abercrombie", "Abercrombie", "Calvin Klein"],
                    "menWomen": ["men", "women", "men"],
                    "size_greater_than_average": [1, 0, 1],
                }
            ),
        ),
    ],
)
def test_get_sum_score_by_brand_and_gender(input_frame, expected_result):
    # This check compares a grouped DataFrame, not just a single column.
    output_frame = get_sum_score_by_brand_and_gender(
        input_frame, "brand", "menWomen", "size_greater_than_average"
    )
    assert_frame_equal(output_frame, expected_result)
    assert isinstance(output_frame, pd.DataFrame)
