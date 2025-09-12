import pandas as pd

def prefix_labels(data, prefix):
    if isinstance(data, pd.Series):
        data.index = prefix + data.index.astype(str)
    elif isinstance(data, pd.DataFrame):
        data.columns = prefix + data.columns.astype(str)
    return data

# Example usage:
# For Series
series_example = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
prefixed_series = prefix_labels(series_example, 'prefix_')
print(prefixed_series)

# For DataFrame
df_example = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [4, 5, 6]
})
prefixed_df = prefix_labels(df_example, 'prefix_')
print(prefixed_df)
