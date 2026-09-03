"""Reference solution for the transformation helpers."""

import pandas as pd


def is_greater_than_average(series: pd.Series) -> pd.Series:
    """Return 0 for values <= mean, else 1."""
    average = series.mean()
    return pd.Series([0 if value <= average else 1 for value in series])


def get_sum_score_by_brand_and_gender(
    frame: pd.DataFrame,
    brand_col="brand",
    gender_col="menWomen",
    score_by="size_greater_than_average",
) -> pd.DataFrame:
    """Groups by brand and gender, then sums the score column."""
    return frame.groupby(by=[brand_col, gender_col], as_index=False)[score_by].sum()
