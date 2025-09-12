import pandas as pd

def check_series_equal(left, right, check_like=False):
    if check_like:
        return pd.testing.assert_series_equal(left, right, check_names=True, check_index_type=True, check_dtype=True, check_extension=True, check_category=True, check_like=True)
    else:
        return pd.testing.assert_series_equal(left, right)
