import pandas as pd

# Sample DataFrame
data = {
    'A': [None, 2, 3, None],
    'B': [None, None, None, 4],
    'C': [0, None, 1, None]
}

df = pd.DataFrame(data)

# Function to compute the first non-null entry of each column
def first_non_null(df):
    return df.apply(lambda col: col.first_valid_index()).apply(lambda idx: df.loc[idx] if pd.notna(idx) else None)

# Get the first non-null entries
first_non_null_entries = first_non_null(df)
print(first_non_null_entries)
