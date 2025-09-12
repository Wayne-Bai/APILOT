import pandas as pd

def check_like(series1, series2):
    return series1.equals(series2)

# usage:
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([1, 2, 3])
assert_series_equal(series1, series2, check_like=check_like)
