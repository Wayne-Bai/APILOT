import pandas as pd

# Sample DataFrame
data = {
    'A': [None, 2, 3, 4],
    'B': [5, None, 7, 8],
    'C': [None, None, 11, None]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda col: col[col.first_valid_index()])
print(first_non_null)
