import pandas as pd

# Assume df is your DataFrame
def first_min_index(df, axis=0):
    # If axis is 0, find the first occurrence of the minimum value in each column
    # If axis is 1, find the first occurrence of the minimum value in each row

    if axis == 0:
        return df.idxmin()
    elif axis == 1:
        return df.idxmin(axis=1)
    else:
        raise ValueError("Axis must be 0 or 1")
