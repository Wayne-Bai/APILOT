import pandas as pd

# Example usage
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([1, 2, 3])
pd.testing.assert_series_equal(series1, series2, check_like=True)
