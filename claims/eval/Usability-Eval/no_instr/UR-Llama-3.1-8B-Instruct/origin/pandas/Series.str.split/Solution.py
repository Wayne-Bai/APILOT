import pandas as pd

def split_strings(df, col, sep):
    """
    Split strings in a pandas DataFrame column around a given separator.

    Parameters:
    - df (pandas DataFrame): The DataFrame containing the column to split.
    - col (str): The name of the column to split.
    - sep (str): The separator around which to split the strings.

    Returns:
    - pandas DataFrame: The DataFrame with the split column.
    """
    # Split the strings using the str.split method
    df[col] = df[col].str.split(sep)

    return df

# Example usage:
data = {'Name': ['John,Anna,Mary', 'David,Betty,Sarah', 'Peter,Jane,Dave'],
        'Age': [28, 35, 32]}
df = pd.DataFrame(data)

print("Before Split:")
print(df)

df = split_strings(df, 'Name', ',')

print("\nAfter Split:")
print(df)
