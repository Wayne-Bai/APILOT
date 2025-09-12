import pandas as pd

# Given dataframe df
# n is the number of rows to return

def get_first_n_rows(df, n):
    return df.head(n)
