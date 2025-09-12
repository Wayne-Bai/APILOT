import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 6]
}

df = pd.DataFrame(data)

# Find the index of the first occurrence of the maximum value over rows for each column
max_indices_over_rows = df.idxmax(axis=0)

# Find the index of the first occurrence of the maximum value over columns for each row
max_indices_over_columns = df.idxmax(axis=1)

print("Index of first occurrence of maximum over rows for each column:")
print(max_indices_over_rows)

print("\nIndex of first occurrence of maximum over columns for each row:")
print(max_indices_over_columns)
