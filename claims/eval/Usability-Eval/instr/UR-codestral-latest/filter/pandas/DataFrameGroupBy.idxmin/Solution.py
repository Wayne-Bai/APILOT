import pandas as pd
import numpy as np

# Assuming df is your DataFrame and axis=0 for rows and axis=1 for columns
def first_min_index(df, axis=0):
    if axis == 0:
        # Exclude NA/null values and find the index of the minimum value in each column
        return df.replace([np.inf, -np.inf], np.nan).idxmin(axis=axis)
    elif axis == 1:
        # Exclude NA/null values and find the index of the minimum value in each row
        return df.replace([np.inf, -np.inf], np.nan).idxmin(axis=axis)
    else:
        raise ValueError("Axis value should be 0 or 1")
