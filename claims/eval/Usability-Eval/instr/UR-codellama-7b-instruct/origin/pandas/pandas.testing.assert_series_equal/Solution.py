import pandas as pd

# Create two sample series for testing
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Use the assert_series_equal function with check_like=True to compare the series
pd.testing.assert_series_equal(s1, s2, check_like=True)
