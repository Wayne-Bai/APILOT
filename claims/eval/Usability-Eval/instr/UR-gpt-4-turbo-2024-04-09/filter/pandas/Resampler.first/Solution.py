import pandas as pd

# Sample DataFrame creation
data = {
    'A': [None, None, 5, 7],
    'B': [1, None, None, 2],
    'C': [None, 8, 9, 10],
    'D': [None, None, None, None]  # A column with all nulls
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.bfill().iloc[0]

print(first_non_null)
