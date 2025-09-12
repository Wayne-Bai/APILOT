import pandas as pd

def group_quantiles(df, group_col, target_col, quantiles):
    """
    Return group values at the given quantile.

    Parameters:
    df (DataFrame): The input DataFrame.
    group_col (str): The column name to group by.
    target_col (str): The column name to calculate quantiles on.
    quantiles (list): A list of quantiles to compute (between 0 and 1).

    Returns:
    DataFrame: A DataFrame with group names and corresponding quantiles.
    """
    return df.groupby(group_col)[target_col].quantile(quantiles).unstack()

# Example usage:
# df = pd.DataFrame({
#     'group': ['A', 'A', 'B', 'B', 'C', 'C'],
#     'value': [1, 2, 3, 4, 5, 6]
# })
# quantiles = [0.25, 0.5, 0.75]
# result = group_quantiles(df, 'group', 'value', quantiles)
# print(result)
