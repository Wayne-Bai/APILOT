import pandas as pd

# Prefix for Series
def prefix_series(s, prefix):
    return pd.Series(s.values, index=prefix + s.index)

# Prefix for DataFrame
def prefix_dataframe(df, prefix):
    return df.rename(columns={col: prefix + col for col in df.columns})

# Example usage:
# series = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# prefixed_series = prefix_series(series, 'Prefix_')
# print(prefixed_series)

# dataframe = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# prefixed_dataframe = prefix_dataframe(dataframe, 'Prefix_')
# print(prefixed_dataframe)
