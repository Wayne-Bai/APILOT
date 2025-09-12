import pandas as pd

def check_like(df1, df2):
    return df1.equals(df2)

pd.testing.assert_series_equal(df1, df2, check_like=check_like)
