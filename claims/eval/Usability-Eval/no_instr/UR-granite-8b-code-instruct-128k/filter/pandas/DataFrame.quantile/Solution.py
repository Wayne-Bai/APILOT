import pandas as pd

def quantile_over_axis(df, quantile, axis):
    return df.quantile(quantile, axis=axis)
