import pandas as pd

# Sample DataFrame
data = {
    'A': [3, 1, 2, 5],
    'B': [7, 2, 3, 4],
    'C': [5, 8, 5, 1]
}

df = pd.DataFrame(data)

# Get index of first occurrence of maximum value over columns (axis=0)
max_index_col = df.idxmax(axis=0)

# Get index of first occurrence of maximum value over rows (axis=1)
max_index_row = df.idxmax(axis=1)

print("Index of first occurrence of maximum value over columns:", max_index_col)
print("Index of first occurrence of maximum value over rows:", max_index_row)
