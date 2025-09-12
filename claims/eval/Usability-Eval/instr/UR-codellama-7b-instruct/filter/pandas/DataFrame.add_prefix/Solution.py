
import pandas as pd

# Function to prefix labels for a Series or DataFrame
def prefix_labels(df):
    # Check if input is a Series or a DataFrame
    if isinstance(df, pd.Series):
        # Prefix the row labels
        df.index = ['prefix' + str(i) for i in df.index]
    elif isinstance(df, pd.DataFrame):
        # Prefix the column labels
        df.columns = ['prefix' + str(i) for i in df.columns]
    else:
        raise ValueError("Input must be a Series or a DataFrame")
