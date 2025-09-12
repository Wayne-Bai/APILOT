import pandas as pd

def pairwise_correlation(df):
    return df.corr(method='pearson', min_periods=1)
