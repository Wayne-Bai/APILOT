import pandas as pd

# Suppose we have a DataFrame `df` and we want to find the index of the first occurrence of the minimum value along a specified axis.
def first_min_index(df, axis):
    # Drop NA/null values along the specified axis
    clean_df = df.replace({pd.NA: None}).dropna(axis=axis)

    # Find the index of the first occurrence of the minimum value along the specified axis
    min_index = clean_df.idxmin(axis=axis).iloc[0] if clean_df.shape[0] > 0 else None

    return min_index

# Example usage:
data = {'A': [4, 3, 6, 2], 'B': [1, 2, 3, 4], 'C': [3, 3, 6, 7]}
df = pd.DataFrame(data)
axis = 0
index = first_min_index(df, axis)
print(index)
