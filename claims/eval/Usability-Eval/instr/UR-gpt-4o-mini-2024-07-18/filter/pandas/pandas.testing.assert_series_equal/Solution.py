import pandas as pd

# Example Series to compare
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([1, 2, 3, 4, 5])

# Using the updated function to check for equality
pd.testing.assert_series_equal(series1, series2, check_like=True)
