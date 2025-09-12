import pandas as pd

def find_first_max(df):
    return df.idxmax().iloc[0]
