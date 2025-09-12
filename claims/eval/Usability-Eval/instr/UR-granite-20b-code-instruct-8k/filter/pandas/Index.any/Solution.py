import pandas as pd

def check_any_truthy(df):
    """
    Check whether any element in the DataFrame is Truthy.
    
    Parameters:
    df (pandas.DataFrame): Input DataFrame
    
    Returns:
    bool: True if any element is Truthy, False otherwise
    """
    return df.any()
