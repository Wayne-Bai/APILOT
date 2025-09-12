
import pandas as pd

def assert_series_equal(left, right, check_like=False):
    if check_like:
        if not left.equals(right):
            raise AssertionError("Series are not equal")
    else:
        pd.testing.assert_series_equal(left, right)

# Example usage
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([1, 2, 3])
assert_series_equal(s1, s2, check_like=True)
