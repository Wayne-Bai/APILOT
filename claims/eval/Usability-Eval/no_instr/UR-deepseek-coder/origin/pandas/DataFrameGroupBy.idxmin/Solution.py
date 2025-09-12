import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [3, 3, 3, 3, 3]
}
df = pd.DataFrame(data)

# Function to return the index of the first occurrence of the minimum over the requested axis
def first_min_index(df, axis=0):
    if axis == 0:
        return df.apply(lambda col: col.dropna().idxmin())
    elif axis == 1:
        return df.apply(lambda row: row.dropna().idxmin(), axis=1)
    else:
        raise ValueError("Axis must be 0 or 1")

# Example usage
min_indices = first_min_index(df, axis=0)
print(min_indices)
