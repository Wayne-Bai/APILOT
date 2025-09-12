import pandas as pd
import numpy as np

def assert_series_equal(left, right, check_like=False, **kwargs):
    if check_like:
        # Check if the series have the same shape and data types
        if not (left.shape == right.shape and left.dtype == right.dtype):
            raise AssertionError("Series do not have the same shape or data types")

        # Check if the series have the same values, considering NaN as equal
        if not (left.fillna('NaN') == right.fillna('NaN')).all():
            raise AssertionError("Series do not have the same values")

    else:
        # Perform a standard comparison of the series
        if not (left == right).all():
            raise AssertionError("Series are not equal")

# Example usage:
if __name__ == "__main__":
    # Create sample pandas series
    s1 = pd.Series([1, 2, np.nan, 4])
    s2 = pd.Series([1, 2, np.nan, 4])
    s3 = pd.Series([1, 2, np.nan, 5])

    # Assert that s1 and s2 are equal, considering NaN as equal
    assert_series_equal(s1, s2, check_like=True)

    # Assert that s1 and s3 are equal, considering NaN as equal
    try:
        assert_series_equal(s1, s3, check_like=True)
    except AssertionError as e:
        print(e)

    # Perform a standard comparison of s1 and s3
    try:
        assert_series_equal(s1, s3)
    except AssertionError as e:
        print(e)
