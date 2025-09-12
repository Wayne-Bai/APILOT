import pandas as pd

def assert_series_equal(actual, desired, check_like=False):
    if check_like:
        actual = actual.apply(lambda x: x if isinstance(x, str) else str(x))
        desired = desired.apply(lambda x: x if isinstance(x, str) else str(x))
    pd.testing.assert_series_equal(actual, desired)
