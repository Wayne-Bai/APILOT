import pandas as pd
from pandas.testing import assert_series_equal

# Sample data for demonstration
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([3, 2, 1], index=['c', 'b', 'a'])

# Use assert_series_equal with check_like=True to ignore index order
assert_series_equal(series1, series2, check_like=True)

print("Both series are equal with check_like=True.")
