import pandas as pd

# Function to prefix labels with a string prefix
def prefix_labels(data, prefix):
    if isinstance(data, pd.Series):
        # Prefixing the index of a Series
        data.index = prefix + data.index.astype(str)
    elif isinstance(data, pd.DataFrame):
        # Prefixing the column labels of a DataFrame
        data.columns = prefix + data.columns.astype(str)
    else:
        raise TypeError("Input must be a pandas Series or DataFrame")
    
    return data

# Example usage:
# Creating a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Creating a Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Apply prefix
df_prefixed = prefix_labels(df, 'col_')
s_prefixed = prefix_labels(s, 'row_')

print("DataFrame with prefixed columns:")
print(df_prefixed)
print("\nSeries with prefixed index:")
print(s_prefixed)
