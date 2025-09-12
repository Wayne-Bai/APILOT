import pandas as pd

def first_non_null_entry(df):
    """
    This function takes a DataFrame as input and returns a new DataFrame with the first non-null entry of each column.
    """
    # Create a new DataFrame with the first non-null entry of each column
    first_non_null = df.iloc[:, df.columns].apply(lambda x: x.dropna().iloc[0], axis=1)

    return first_non_null
