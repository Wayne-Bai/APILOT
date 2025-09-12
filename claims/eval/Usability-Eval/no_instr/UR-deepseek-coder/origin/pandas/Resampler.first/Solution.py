import pandas as pd

# Sample DataFrame
data = {
    'A': [None, 2, 3, 4],
    'B': [1, None, 3, 4],
    'C': [None, None, 3, 4],
    'D': [1, 2, None, 4]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null_entries = df.apply(lambda col: col.dropna().iloc[0] if not col.dropna().empty else None)

print(first_non_null_entries)
