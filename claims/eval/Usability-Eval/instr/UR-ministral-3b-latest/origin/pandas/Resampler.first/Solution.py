import pandas as pd

# Assuming df is the DataFrame containing the data
df = pd.DataFrame({'A': [1, None, 2], 'B': [None, 3, None], 'C': [4, 5, None]})

# Compute the first non-null entry of each column
first_non_null_entries = df.notnull().any().idxmin().dropna()

for column in first_non_null_entries:
    first_non_null = df.loc[first_non_null_entries[column].to_list(0)[0], column]
    print(f"First non-null entry in column '{column}': {first_non_null}")
