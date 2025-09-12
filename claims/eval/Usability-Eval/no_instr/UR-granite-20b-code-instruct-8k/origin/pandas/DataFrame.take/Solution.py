import pandas as pd

def return_positional_indices(df, axis, indices):
    return df.iloc[indices,] if axis == 0 else df.iloc[:,indices]
