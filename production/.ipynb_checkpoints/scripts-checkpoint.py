"""Module for listing down additional custom functions required for production."""

import pandas as pd

def binned_median_income(df):
    """Bin the median income column using quantiles."""
    return pd.qcut(df["median_income"], q=5)