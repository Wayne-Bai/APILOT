import pandas as pd

def hide_columns(df, columns):
    """
    Hide specific columns from display.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    columns (list): List of column names to hide.

    Returns:
    pd.DataFrame: Modified dataframe with specified columns hidden.
    """
    # Copy the dataframe to prevent in-place modification
    df = df.copy()

    # Hide specified columns
    display(df[~df.columns.isin(columns)])

    return df

# Example usage
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6], 'Column3': [7, 8, 9]}
df = pd.DataFrame(data)

hidden_df = hide_columns(df, ['Column1', 'Column2'])
print(hidden_df)
