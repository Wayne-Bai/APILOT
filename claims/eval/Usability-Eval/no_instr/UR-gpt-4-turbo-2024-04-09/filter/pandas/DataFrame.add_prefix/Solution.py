import pandas as pd

def prefix_labels(data, prefix):
    if isinstance(data, pd.Series):
        # Prefixing row labels for a Series
        data.index = prefix + data.index.astype(str)
    elif isinstance(data, pd.DataFrame):
        # Prefixing column labels for a DataFrame
        data.columns = prefix + data.columns.astype(str)
    return data

# Example usage with DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Example usage with Series
s = pd.Series([1, 2, 3], index=['x', 'y', 'z'])

# Applying prefix to DataFrame and Series
prefixed_df = prefix_labels(df, 'col_')
prefixed_s = prefix_labels(s, 'row_')

print("DataFrame with Prefixed Columns:\n", prefixed_df)
print("Series with Prefixed Index:\n", prefixed_s)
