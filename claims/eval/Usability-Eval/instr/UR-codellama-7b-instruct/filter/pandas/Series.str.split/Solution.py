import pandas as pd

def split_strings(df, col_name, sep):
    """
    Splits a column of strings in a dataframe into multiple columns based on a given separator (e.g., comma).
    
    Parameters:
    df (pandas.DataFrame): The dataframe containing the string column to be split.
    col_name (str): The name of the column to be split.
    sep (str): The separator or delimiter to use for splitting.
    
    Returns:
    pandas.DataFrame: A new dataframe with the split columns.
    """
    # create a new dataframe with the same index and column names as the input dataframe
    output_df = pd.DataFrame(index=df.index, columns=df.columns)
    
    # split the string column into multiple columns using the specified separator
    split_values = df[col_name].str.split(sep, expand=True)
    
    # add the split values to the new dataframe
    output_df[col_name] = split_values
    
    return output_df