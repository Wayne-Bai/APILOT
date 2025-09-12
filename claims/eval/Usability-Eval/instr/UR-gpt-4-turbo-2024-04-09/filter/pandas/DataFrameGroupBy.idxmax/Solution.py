import pandas as pd

# Creating a DataFrame for demonstration
data = {
    'A': [1, 5, 2, 8, 4],
    'B': [12, 7, 9, 1, 11]
}

df = pd.DataFrame(data)

# Get the index of the first occurrence of the maximum value over the default axis (column-wise)
max_index_columns = df.idxmax()

# To find the index of the first occurrence of the maximum value row-wise
max_index_rows = df.apply(lambda x: x.idxmax(), axis=1)

# Showing results
print("Index of first occurrence of maximum over columns:")
print(max_index_columns)
print("\nIndex of first occurrence of maximum over rows:")
print(max_index_rows)
