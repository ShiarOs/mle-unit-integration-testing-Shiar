import pandas as pd


def impute_mean(series: pd.Series) -> pd.Series:
    """Impute missing values with the series mean.

    This keeps the overall average stable for numeric columns.
    """

    return series.fillna(series.mean())


def impute_min(series: pd.Series) -> pd.Series:
    """Impute missing values with the series minimum.

    Useful when you want a conservative lower-bound fallback.
    """

    return series.fillna(series.min())


def impute_max(series: pd.Series) -> pd.Series:
    """Impute missing values with the series maximum.

    Useful when you want an upper-bound fallback.
    """

    return series.fillna(series.max())
