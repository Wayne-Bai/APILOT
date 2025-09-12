import pandas as pd

# Sample DataFrame
data = {
    'A': [3, 1, 2],
    'B': [5, 4, 1]
}

df = pd.DataFrame(data)

# Get the index of the first occurrence of the minimum value in each column (axis=0)
min_index_per_column = df.idxmin(axis=0)

# Get the index of the first occurrence of the minimum value in each row (axis=1)
min_index_per_row = df.idxmin(axis=1)

print("Index of the first occurrence of the minimum in each column:")
print(min_index_per_column)

print("\nIndex of the first occurrence of the minimum in each row:")
print(min_index_per_row)
