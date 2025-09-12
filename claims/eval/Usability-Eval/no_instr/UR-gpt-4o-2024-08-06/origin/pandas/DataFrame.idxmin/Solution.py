import pandas as pd

# Sample data
data = {
    'A': [4, 2, 0, 3],
    'B': [10, 20, 30, 40],
    'C': [15, 1, 1, 6]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Return index of the first occurrence of minimum value for each column
first_min_index_col = df.idxmin(axis=0)

# Return index of the first occurrence of minimum value for each row
first_min_index_row = df.idxmin(axis=1)

print("Index of first occurrence of minimum for each column:")
print(first_min_index_col)

print("\nIndex of first occurrence of minimum for each row:")
print(first_min_index_row)
