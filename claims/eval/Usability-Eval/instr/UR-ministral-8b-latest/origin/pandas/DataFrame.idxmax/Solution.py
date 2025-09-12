import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 1, 4, 5]
}
df = pd.DataFrame(data)

# Function to return the index of the first occurrence of maximum along a specified axis
def first_max_index(df, axis):
    if axis not in [0, 1]:
        raise ValueError("Axis must be 0 (rows) or 1 (columns)")

    max_values = df.idxmax(axis=axis)
    if axis == 0:
        result = []
        for col in df.columns:
            result.append(max_values[col].iloc[0])
        return result
    else:
        for row in df.index:
            result = df.loc[row].idxmax().iloc[0]
        return result

# Test the function
axis = 0  # Use 0 for rows, 1 for columns
print(first_max_index(df, axis))
