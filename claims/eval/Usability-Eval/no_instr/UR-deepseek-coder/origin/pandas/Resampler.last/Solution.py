import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4, None],
    'B': [None, 2, 3, None, 5],
    'C': [1, None, None, 4, 5]
}

df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null_entries = df.apply(lambda col: col.dropna().iloc[-1])

print(last_non_null_entries)
