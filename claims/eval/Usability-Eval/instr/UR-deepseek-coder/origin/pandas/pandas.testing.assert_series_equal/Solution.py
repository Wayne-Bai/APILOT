import pandas as pd

def assert_series_equal(left, right, check_like=False):
    if check_like:
        # Check if the series are equal in a "like" manner, ignoring order of indices
        left_sorted = left.sort_index()
        right_sorted = right.sort_index()
        pd.testing.assert_series_equal(left_sorted, right_sorted)
    else:
        # Check if the series are exactly equal
        pd.testing.assert_series_equal(left, right)

# Example usage:
# s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# s2 = pd.Series([1, 2, 3], index=['c', 'b', 'a'])
# assert_series_equal(s1, s2, check_like=True)  # This should pass
# assert_series_equal(s1, s2)  # This should raise an AssertionError
