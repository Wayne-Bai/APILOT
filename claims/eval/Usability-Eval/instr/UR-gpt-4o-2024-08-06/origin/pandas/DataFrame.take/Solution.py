import pandas as pd

# Function to return elements at given positional indices along an axis
def return_elements_by_indices(data, indices, axis=0):
    """
    Select elements along a specified axis by their positional indices.
    
    :param data: Input data (DataFrame or Series)
    :param indices: List of positional indices to select
    :param axis: Axis along which to select. 0 for rows, 1 for columns
    :return: Subset of data with elements at specified indices
    """
    if axis == 0:  # Select rows by indices if axis is 0
        return data.iloc[indices]
    elif axis == 1:  # Select columns by indices if axis is 1
        return data.iloc[:, indices]
    else:
        raise ValueError("Axis must be 0 (rows) or 1 (columns)")

# Example usage:
# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Get rows with indices 0 and 2
result_rows = return_elements_by_indices(df, [0, 2], axis=0)

# Get columns with indices 0 and 2
result_columns = return_elements_by_indices(df, [0, 2], axis=1)

print("Rows at indices 0 and 2:\n", result_rows, "\n")
print("Columns at indices 0 and 2:\n", result_columns)
