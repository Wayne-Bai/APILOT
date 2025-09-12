import pandas as pd

def map_values(df, mapping):
    """
    This function maps values in a pandas DataFrame using an input mapping or function.

    Parameters:
    df (DataFrame): The input DataFrame.
    mapping (dict or function): A dictionary mapping old values to new values, or a function that takes an old value and returns a new value.

    Returns:
    DataFrame: The DataFrame with mapped values.
    """
    if isinstance(mapping, dict):
        return df.replace(mapping)
    elif callable(mapping):
        return df.applymap(mapping)
    else:
        raise ValueError("Mapping must be a dictionary or a function.")

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# mapping = {1: 'one', 2: 'two', 3: 'three'}
# df_mapped = map_values(df, mapping)
