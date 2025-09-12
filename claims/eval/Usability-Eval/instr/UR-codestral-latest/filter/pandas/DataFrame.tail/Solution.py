# Importing pandas library
import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to return
def get_last_n_rows(df, n):
    return df.tail(n)
