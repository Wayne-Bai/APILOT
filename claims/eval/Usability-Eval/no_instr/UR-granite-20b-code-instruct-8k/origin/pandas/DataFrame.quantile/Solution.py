import pandas as pd

def return_values_at_given_quantile(df, quantile):
    return df.quantile(quantile)
