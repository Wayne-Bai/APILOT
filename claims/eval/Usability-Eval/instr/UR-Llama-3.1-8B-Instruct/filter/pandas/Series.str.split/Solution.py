import pandas as pd

def split_strings(df, column, separator):
    """
    Splits strings in a pandas DataFrame column around a given separator/delimiter.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column (str): The column name to split.
    separator (str): The separator/delimiter to split the strings around.
    
    Returns:
    pd.DataFrame: The input DataFrame with the specified column split into separate columns.
    """
    # Use pd.Series.str.split with an expansion parameter to create new columns
    df = df.assign(**{column: df[column].str.split(separator, expand=True)})
    
    # Drop the original column and return the modified DataFrame
    return df.drop(columns=[column])

# Example usage
data = {
    'Names': ['John,Smith', 'Jane,Brown', 'Bob,Perez']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = split_strings(df, 'Names', ',')
print("\nDataFrame after splitting column 'Names' around comma:")
print(df)
