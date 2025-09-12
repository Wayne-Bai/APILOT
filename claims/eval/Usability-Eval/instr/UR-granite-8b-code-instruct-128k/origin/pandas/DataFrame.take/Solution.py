
import pandas as pd

def return_positional_indices(df, indices, axis=0):
    return df.iloc[indices, axis]
