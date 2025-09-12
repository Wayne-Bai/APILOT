import pandas as pd

def get_elements_at_indices(df, indices, axis=0):
    if axis == 0:
        return df.iloc[indices]
    elif axis == 1:
        return df.iloc[:, indices]
    else:
        raise ValueError("Axis must be 0 or 1")

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
# indices = [0, 2]
# result = get_elements_at_indices(df, indices, axis=0)
# print(result)
