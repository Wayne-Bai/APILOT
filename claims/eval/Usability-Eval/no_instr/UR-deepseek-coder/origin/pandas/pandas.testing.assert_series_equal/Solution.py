import pandas as pd

def assert_series_equal(left, right, check_like=False):
    if check_like:
        pd.testing.assert_series_equal(left.sort_index(), right.sort_index(), check_exact=False, check_names=False)
    else:
        pd.testing.assert_series_equal(left, right)

# Example usage:
# series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# series2 = pd.Series([1, 2, 3], index=['c', 'b', 'a'])
# assert_series_equal(series1, series2, check_like=True)
