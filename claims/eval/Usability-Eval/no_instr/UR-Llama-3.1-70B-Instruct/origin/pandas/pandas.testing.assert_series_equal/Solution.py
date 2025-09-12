import pandas as pd
import pandas.testing as pd_testing
import numpy as np

# Create two sample series for testing
series1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
series2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Test using assert_series_equal with check_like=True
try:
    pd_testing.assert_series_equal(series1, series2, check_like=True)
    print("Series are equal.")
except AssertionError as e:
    print("Series are not equal:", e)

# Create two sample series with different indices but same values
series1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
series2 = pd.Series([1, 2, 3, 4, 5], index=['f', 'g', 'h', 'i', 'j'])

# Test using assert_series_equal with check_like=True (False by default)
try:
    pd_testing.assert_series_equal(series1, series2, check_like=True)
    print("Series are equal.")
except AssertionError as e:
    print("Series are not equal:", e)

# Test using assert_series_equal with check_like=False
try:
    pd_testing.assert_series_equal(series1, series2, check_like=False)
    print("Series are equal when ignoring indices.")
except AssertionError as e:
    print("Series are not equal when ignoring indices:", e)

# Create two sample series with different values but same index
series1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
series2 = pd.Series([5, 4, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])

# Test using assert_series_equal with check_like=True
try:
    pd_testing.assert_series_equal(series1, series2, check_like=True)
    print("Series are equal.")
except AssertionError as e:
    print("Series are not equal:", e)
