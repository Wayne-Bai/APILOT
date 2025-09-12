import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4, 5],
    'B': [7, 8, 9, None, 11],
    'C': [None, 13, 14, 15, 16]
}

df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_nonnull_entries = df.apply(lambda x: x[~x.isna()].tail(1).values[0], axis=0)

print(last_nonnull_entries)
