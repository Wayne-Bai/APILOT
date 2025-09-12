import pandas as pd

# Sample data for demonstration
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [None, None, None, None]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null_entries = df.apply(lambda x: x.dropna().iloc[0])

print(first_non_null_entries)
