import pandas as pd

# Example DataFrame
data = {
    'A': [3, 2, 2, 4],
    'B': [1, 3, 1, 2],
    'C': [4, 1, 3, 1]
}

df = pd.DataFrame(data)

# Function to return the index of the first occurrence of the minimum over the requested axis
def first_min_index(df, axis=0):
    if axis == 0:
        return df.idxmin(axis=axis)
    elif axis == 1:
        return df.idxmin(axis=axis)
    else:
        raise ValueError("Axis must be 0 or 1")

# Example usage
print(first_min_index(df, axis=0))  # Over columns (axis=0)
print(first_min_index(df, axis=1))  # Over rows (axis=1)
