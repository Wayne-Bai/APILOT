import pandas as pd

def prefix_labels(data, prefix):
    if isinstance(data, pd.Series):
        data.index = [f"{prefix}{label}" for label in data.index]
    elif isinstance(data, pd.DataFrame):
        data.columns = [f"{prefix}{label}" for label in data.columns]
    return data

# Example usage for Series
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
prefixed_series = prefix_labels(series, 'prefix_')
print(prefixed_series)

# Example usage for DataFrame
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
prefixed_df = prefix_labels(df, 'prefix_')
print(prefixed_df)
