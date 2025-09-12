import pandas as pd

def split_strings(df, column, separator):
    """
    This function splits strings in a given column of a DataFrame based on a specified separator.

    Parameters:
    df (DataFrame): The input DataFrame.
    column (str): The column name to be split.
    separator (str): The separator used to split the strings.

    Returns:
    DataFrame: A new DataFrame with the split strings.
    """
    df[column] = df[column].str.split(separator)
    return df
