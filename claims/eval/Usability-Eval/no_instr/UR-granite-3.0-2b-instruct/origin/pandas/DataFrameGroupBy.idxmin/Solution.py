import pandas as pd

def find_first_index(df, axis):
    if axis == 0:
        return df.min().idxmin()
    else:
        return df.min(axis=axis).idxmin(axis=axis)

# Example usage:
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 2, 3, 4, 5]
})

print(find_first_index(df, 0))  # Index of first occurrence of minimum in the first axis
print(find_first_index(df, 1))  # Index of first occurrence of minimum in the second axis
