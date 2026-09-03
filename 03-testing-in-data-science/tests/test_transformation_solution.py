"""Regression tests for the reference transformation helpers."""

import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
from src.data_pipeline.transformation_solution import (
    get_sum_score_by_brand_and_gender,
    is_greater_than_average,
)


def test_is_greater_than_average_solution():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    expected_result = pd.Series([0, 0, 1, 0, 1])

    assert_series_equal(is_greater_than_average(input_series), expected_result)


def test_get_sum_score_by_brand_and_gender_solution():
    input_frame = pd.DataFrame(
        {
            "brand": ["Abercrombie", "Abercrombie", "Abercrombie", "Calvin Klein"],
            "menWomen": ["men", "men", "women", "men"],
            "size_greater_than_average": [1, 1, 0, 1],
        }
    )
    expected_result = pd.DataFrame(
        {
            "brand": ["Abercrombie", "Abercrombie", "Calvin Klein"],
            "menWomen": ["men", "women", "men"],
            "size_greater_than_average": [2, 0, 1],
        }
    )

    assert_frame_equal(
        get_sum_score_by_brand_and_gender(input_frame),
        expected_result,
    )
