import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'A': [3, 2, np.nan, 1, 5],
    'B': [np.nan, 1, 2, 4, 0],
    'C': [4, 5, 6, np.nan, 7]
}
df = pd.DataFrame(data)

# Function to find index of first occurrence of minimum value over each column, ignoring NA/null values
def first_min_index(df):
    min_indices = {}
    for column in df.columns:
        non_null_series = df[column].dropna()
        min_index = non_null_series.idxmin() if not non_null_series.empty else None
        min_indices[column] = min_index
    return min_indices

# Get the index of the first occurrence of the minimum value for each column
first_min_indices = first_min_index(df)
print(first_min_indices)
