import pandas as pd

# Sample Series for demonstration
series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
series2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# Using assert_series_equal with check_like argument
pd.testing.assert_series_equal(series1, series2, check_like=True)
