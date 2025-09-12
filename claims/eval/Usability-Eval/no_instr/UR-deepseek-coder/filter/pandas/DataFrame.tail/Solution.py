import pandas as pd

def get_last_n_rows(df, n):
    return df.tail(n)
