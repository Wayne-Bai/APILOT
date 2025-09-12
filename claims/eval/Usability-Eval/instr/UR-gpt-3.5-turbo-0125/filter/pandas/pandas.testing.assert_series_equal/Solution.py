
import pandas as pd

def assert_series_equal(series1, series2, check_like=False):
    if check_like:
        assert series1.equals(series2), "Series are not equal"
    else:
        assert series1.index.equals(series2.index), "Series indices are not equal"
        assert series1.values.tolist() == series2.values.tolist(), "Series values are not equal"
    
# Example usage:
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
assert_series_equal(series1, series2, check_like=True)
