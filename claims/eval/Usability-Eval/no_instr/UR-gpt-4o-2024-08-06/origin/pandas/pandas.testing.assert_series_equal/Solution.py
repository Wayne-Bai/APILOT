import pandas as pd
from pandas.testing import assert_series_equal

# Example series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([3, 2, 1], index=['c', 'b', 'a'])

# Check if two series are equal with check_like=True
assert_series_equal(s1, s2, check_like=True)

print("The two series are equal when index order is ignored.")
