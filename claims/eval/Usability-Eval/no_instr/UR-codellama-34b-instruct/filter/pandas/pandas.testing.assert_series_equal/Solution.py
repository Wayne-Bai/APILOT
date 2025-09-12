
import pandas as pd

# create two sample Series objects
s1 = pd.Series([1, 2, 3, 4], name='a')
s2 = pd.Series([5, 6, 7, 8], name='b')

# use check_like=True to compare the values and indexes of the two Series objects
testing.assert_series_equal(s1, s2, check_like=True)
