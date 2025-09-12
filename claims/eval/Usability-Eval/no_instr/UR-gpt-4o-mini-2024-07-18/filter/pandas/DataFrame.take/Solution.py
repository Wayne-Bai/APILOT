import pandas as pd

def select_elements_by_indices(data, indices, axis=0):
    """
    Return the elements in the given positional indices along an axis.

    Parameters:
    data (pd.DataFrame or pd.Series): Input data.
    indices (list): List of positional indices to select elements from.
    axis (int): Axis along which to select elements (0 for rows, 1 for columns).

    Returns:
    pd.DataFrame or pd.Series: The selected elements.
    """
    return data.take(indices, axis=axis)

# Example usage:
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Select first and third rows
selected_rows = select_elements_by_indices(df, [0, 2], axis=0)
print(selected_rows)

# Select first column
selected_columns = select_elements_by_indices(df, [0], axis=1)
print(selected_columns)
