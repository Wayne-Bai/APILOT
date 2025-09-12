import pandas as pd

# Create two Series
series1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
series2 = pd.Series([1, 2, 3], index=["c", "b", "a"])

# Using pd.testing.assert_series_equal with the check_like argument
try:
    pd.testing.assert_series_equal(series1, series2, check_like=True)
    print("The series are equal considering the order of the indices.")
except AssertionError as e:
    print("Assertion error:", e)
