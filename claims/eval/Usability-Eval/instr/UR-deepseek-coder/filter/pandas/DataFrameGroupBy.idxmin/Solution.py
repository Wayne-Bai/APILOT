import pandas as pd

def first_min_index(df, axis=0):
    if axis == 0:
        return df.apply(lambda col: col.dropna().index[0] if not col.dropna().empty else None).dropna().index[0]
    elif axis == 1:
        return df.apply(lambda row: row.dropna().index[0] if not row.dropna().empty else None, axis=1).dropna().index[0]
    else:
        raise ValueError("Axis must be either 0 or 1")

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, None],
#     'B': [4, 5, None, 6],
#     'C': [7, None, 8, 9]
# })
# print(first_min_index(df, axis=0))  # Output will be the index of the first occurrence of minimum over columns
# print(first_min_index(df, axis=1))  # Output will be the index of the first occurrence of minimum over rows
