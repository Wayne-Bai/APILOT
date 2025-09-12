import pandas as pd

def first_min_index(df, axis=0):
    if axis == 0:
        return df.idxmin(axis=axis)
    elif axis == 1:
        return df.T.idxmin(axis=axis)
    else:
        raise ValueError("Invalid axis. Axis should be 0 (for rows) or 1 (for columns).")

# Test with DataFrame
data = {'A': [2, 3, 1, 4, 5], 'B': [7, 1, 3, 4, 5], 'C': [8, 2, 3, 4, 5]}
df = pd.DataFrame(data)
print(df)
index = first_min_index(df, axis=0)
print("The first occurrence of minimum over requested axis is at index: ", index)
