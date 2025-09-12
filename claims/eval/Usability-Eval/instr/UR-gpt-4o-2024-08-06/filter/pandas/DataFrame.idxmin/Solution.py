import pandas as pd

# Example DataFrame
data = {
    'A': [3, 4, 1, 7],
    'B': [6, 2, 5, 1],
    'C': [7, 8, 3, 9]
}
df = pd.DataFrame(data)

# Function to return index of first occurrence of minimum over requested axis
def first_minimum_index(df, axis=0):
    if axis == 0:
        return (df == df.min()).idxmax()
    elif axis == 1:
        return (df == df.min(axis=1)).idxmax(axis=1)
    else:
        raise ValueError("Axis must be 0 or 1")

# Get the index of the first occurrence of the minimum value for each column
min_index_column = first_minimum_index(df, axis=0)

# Get the index of the first occurrence of the minimum value for each row
min_index_row = first_minimum_index(df, axis=1)

print("Index of first minimum value per column:", min_index_column)
print("Index of first minimum value per row:", min_index_row)
