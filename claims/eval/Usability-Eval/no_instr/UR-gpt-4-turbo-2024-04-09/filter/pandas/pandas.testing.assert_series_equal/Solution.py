import pandas as pd

# Create two Series for comparison
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c'])

# Use assert_series_equal with check_like parameter
pd.testing.assert_series_equal(series1, series2, check_like=False)
