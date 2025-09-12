import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None],
    'C': [1, None, None, 4]
}
df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null = df.apply(lambda col: col[col.last_valid_index()])

print(last_non_null)
