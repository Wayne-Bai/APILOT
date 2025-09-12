import pandas as pd

# Sample DataFrame
data = {
    'A': [None, None, 3, 4],
    'B': [None, 5, 6, None],
    'C': [7, None, None, None]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda col: col.dropna().iloc[0])
print(first_non_null)
