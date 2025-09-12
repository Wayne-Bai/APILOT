# Importing the pandas library
import pandas as pd

# Function to append a suffix to dataframe column labels
def append_suffix_to_dataframe_columns(df, suffix):
    df.columns = [f"{c}{suffix}" for c in df.columns]
    return df
