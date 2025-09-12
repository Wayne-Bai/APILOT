import pandas as pd

def quantile(data, axis=0, q=0.5):
    return pd.Series(data).quantile(q, axis=axis)
