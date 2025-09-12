import pandas as pd
import numpy as np

def get_elements_at_positions(df, indices, axis=0):
    """
    Returns the elements of DataFrame or Series at the given positional indices along the specified axis.

    :param df: The DataFrame or Series from which to retrieve elements
    :param indices: List of positional indices
    :param axis: Axis along which to return elements (0 for index, 1 for columns), default is 0
    :return: A DataFrame or Series with elements at the specified positions
    """
    if isinstance(df, pd.Series):
        # If it's a Series we have only one option for axis which is 0
        return df.iloc[indices]
    elif isinstance(df, pd.DataFrame):
        if axis == 0:
            # Return rows at specified indices if axis is 0
            return df.iloc[indices]
        elif axis == 1:
            # Return columns at specified indices if axis is 1
            return df.iloc[:, indices]
    else:
        raise ValueError("Input must be a pandas DataFrame or Series")

# Example usage
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Get rows at positions 1 and 3
result_rows = get_elements_at_positions(df, [1, 3], axis=0)

# Get columns at positions 0 and 2
result_columns = get_elements_at_positions(df, [0, 2], axis=1)

print("Elements at row indices 1 and 3:\n", result_rows)
print("Elements at column indices 0 and 2:\n", result_columns)
