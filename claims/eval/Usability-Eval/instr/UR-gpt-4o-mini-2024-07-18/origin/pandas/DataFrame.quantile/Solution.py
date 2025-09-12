import pandas as pd

def quantile_values(df, quantiles, axis=0):
    return df.quantile(quantiles, axis=axis)
