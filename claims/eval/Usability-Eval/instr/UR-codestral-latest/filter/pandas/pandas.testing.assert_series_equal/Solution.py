import pandas as pd
from pandas.testing import assert_series_equal

# let's assume these are two Series you want to compare
series1 = pd.Series(data=[1, 2, 3, 4, 5])
series2 = pd.Series(data=[1, 2, 3, 4, 5])

# now you can compare the series with the 'check_like' argument
assert_series_equal(series1, series2, check_like=True)
