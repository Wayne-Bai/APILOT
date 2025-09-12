import pandas as pd

def get_group_quantile(df, group_col, value_col, quantile):
    """
    Returns the quantile values for each group in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    group_col (str): The name of the column to group by.
    value_col (str): The name of the column to calculate the quantile for.
    quantile (float): The quantile to calculate (e.g., 0.5 for the median).

    Returns:
    pandas.Series: A series with the quantile values for each group.
    """
    group_quantiles = df.groupby(group_col)[value_col].quantile(quantile)
    return group_quantiles

# Example usage
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)
result = get_group_quantile(df, 'group', 'value', 0.5)
print(result)
