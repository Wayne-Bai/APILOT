import pandas as pd
from pandas._testing import assert_series_equal

# Create two Series objects for testing
ser1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser2 = pd.Series([4, 5, 6], index=['d', 'e', 'f'])

# Use assert_series_equal() with the check_like argument to compare the two Series objects
assert_series_equal(ser1, ser2, check_like=True)
