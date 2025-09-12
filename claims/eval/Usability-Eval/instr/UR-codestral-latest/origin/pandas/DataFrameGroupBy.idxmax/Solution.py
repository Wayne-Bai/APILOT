import pandas as pd

# Assuming df is your DataFrame and axis=0 (rows)
def first_max_index(df):
    max_val = df.max().max() # Get the maximum value
    return df.loc[df.eq(max_val).idxmax()]

# If you want to operate over columns (axis=1), you can use the apply function
def first_max_index_columns(df):
    max_val = df.max(axis=1)
    return df.apply(lambda x: x.idxmax() if x.max() == max_val.max() else None)
