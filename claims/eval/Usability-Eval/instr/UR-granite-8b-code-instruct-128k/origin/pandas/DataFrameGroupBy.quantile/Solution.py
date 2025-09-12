import pandas as pd

def quantile(data, quantile):
    return pd.Series(data).quantile(quantile)
