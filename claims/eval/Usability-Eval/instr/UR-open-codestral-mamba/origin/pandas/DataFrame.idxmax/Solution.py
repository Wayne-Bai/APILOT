import pandas as pd

def index_of_max_over_axis(df, axis):
    return df.idxmax(axis=axis)

# Assuming 'df' is your DataFrame
