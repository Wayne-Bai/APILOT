import pandas as pd
import numpy as np

def group_quantile(df, group_col, value_col, q):
    """
    Return group values at the given quantile.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    group_col (str): The column to group by.
    value_col (str): The column containing the values to calculate the quantile.
    q (float): The quantile to calculate (between 0 and 1).
    
    Returns:
    pd.Series: A Series with the quantile values for each group.
    """
    return df.groupby(group_col)[value_col].apply(lambda x: np.percentile(x, q * 100))

# Example usage:
# data = {'group': ['A', 'A', 'B', 'B', 'B'], 'value': [1, 2, 3, 4, 5]}
# df = pd.DataFrame(data)
# result = group_quantile(df, 'group', 'value', 0.5)
# print(result)
