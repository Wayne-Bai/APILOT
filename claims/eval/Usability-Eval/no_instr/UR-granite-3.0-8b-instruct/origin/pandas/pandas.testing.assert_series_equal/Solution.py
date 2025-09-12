import pandas as pd

def check_series(actual, expected, check_like=False):
    if check_like:
        pd.testing.assert_series_equal(actual, expected, check_like=True)
    else:
        pd.testing.assert_series_equal(actual, expected)

# Example usage:
actual = pd.Series([1, 2, 3])
expected = pd.Series([1, 2, 3])
check_series(actual, expected, check_like=True)
