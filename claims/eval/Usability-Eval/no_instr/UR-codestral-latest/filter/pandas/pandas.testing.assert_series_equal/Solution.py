import pandas as pd

# Create two Series objects for comparison
series1 = pd.Series(data=[1, 2, 3, 4, 5])
series2 = pd.Series(data=[1, 2, 3, 4, 5])

# Use assert_series_equal() with check_like=True to compare the Series objects
pd.testing.assert_series_equal(series1, series2, check_like=True)
