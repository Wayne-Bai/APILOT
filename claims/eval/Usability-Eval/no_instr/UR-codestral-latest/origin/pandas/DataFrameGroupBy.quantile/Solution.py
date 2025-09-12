import pandas as pd

def get_group_quantile(df, group_column, value_column, q):
    """
    This function returns the group values at the given quantile.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    group_column (str): The column name used for grouping.
    value_column (str): The column name from which we want to find the quantile.
    q (float): The quantile to find, ranging from 0 to 1.

    Returns:
    DataFrame: A DataFrame with the group labels and their corresponding quantiles.
    """
    return df.groupby(group_column)[value_column].quantile(q)
