import pandas as pd

def first_max_index(df, axis=0):
    if axis == 0:
        return df.eq(df.max(axis=axis)).idxmax(axis=1).dropna().iloc[0]
    elif axis == 1:
        return df.eq(df.max(axis=axis)).idxmax(axis=0).dropna().iloc[0]
    else:
        raise ValueError("Axis must be 0 or 1")

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4],
#     'B': [2, 3, 4, 1],
#     'C': [3, 4, 1, 2]
# })
# print(first_max_index(df, axis=0))  # Output: Index of the first occurrence of the maximum value in each column
# print(first_max_index(df, axis=1))  # Output: Index of the first occurrence of the maximum value in each row
