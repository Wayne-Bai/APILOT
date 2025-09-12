import pandas as pd

def prefix_labels(data, prefix):
    # Handle DataFrame
    if isinstance(data, pd.DataFrame):
        # Prefix column labels
        data.columns = prefix + data.columns.astype(str)

    # Handle Series
    elif isinstance(data, pd.Series):
        # Prefix row labels
        data.index = prefix + data.index.astype(str)

    return data

# Example usage
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
series = pd.Series([10, 20], index=['a', 'b'])

print("Original DataFrame:")
print(df)
print("\nOriginal Series:")
print(series)

df = prefix_labels(df, 'prefix_')
series = prefix_labels(series, 'prefix_')

print("\nPrefixed DataFrame:")
print(df)
print("\nPrefixed Series:")
print(series)
