import pandas as pd

# Sample data for demonstration
data = {
    'A': [3, 6, 1, 4],
    'B': [2, 4, 9, 3],
    'C': [5, 6, 5, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Find the index of the first occurrence of the maximum value over columns (axis=0)
col_max_index = df.eq(df.max(axis=0)).idxmax(axis=0)
print("Column-wise max index:")
print(col_max_index)

# Find the index of the first occurrence of the maximum value over rows (axis=1)
row_max_index = df.eq(df.max(axis=1), axis=0).idxmax(axis=1)
print("\nRow-wise max index:")
print(row_max_index)
