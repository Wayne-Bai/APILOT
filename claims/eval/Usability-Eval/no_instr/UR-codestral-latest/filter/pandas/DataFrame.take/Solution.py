import pandas as pd

# Let's assume df is your DataFrame and indices is your list of positional indices
# .iloc is used for integer indexing

def get_elements(df, indices):
    return df.iloc[indices]
