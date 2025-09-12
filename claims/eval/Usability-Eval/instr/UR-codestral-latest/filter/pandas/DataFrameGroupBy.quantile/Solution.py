import pandas as pd
import numpy as np

def get_quantile_value(dataframe, column, q):
    """
    This function takes a dataframe, the target column and a quantile as input.
    It then sorts the values in the given column and returns the value at the specified quantile.
    """
    sorted_values = dataframe[column].sort_values(ignore_index=True)
    index = int(q * len(sorted_values))
    return sorted_values[index]

# Example usage:
# df = pd.DataFrame({'Column1': [1, 2, 3, 4, 5]})
# print(get_quantile_value(df, 'Column1', 0.5))
