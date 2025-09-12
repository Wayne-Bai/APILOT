import pandas as pd

def find_min_index(df, axis):
    return df.min(axis=axis).idxmin()
