import pandas as pd

# Prefix for Series index labels
def prefix_series_labels(series, prefix):
    series.index = [f"{prefix}{label}" for label in series.index]
    return series

# Prefix for DataFrame column labels
def prefix_dataframe_labels(df, prefix):
    df.columns = [f"{prefix}{label}" for label in df.columns]
    return df

# Example usage:

# Create example Series
series_example = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# Prefix Series index labels
series_with_prefix = prefix_series_labels(series_example, 'prefix_')
print(series_with_prefix)

# Create example DataFrame
df_example = pd.DataFrame({
    'col1': [1, 2],
    'col2': [3, 4]
}, index=['row1', 'row2'])
# Prefix DataFrame column labels
df_with_prefix = prefix_dataframe_labels(df_example, 'prefix_')
print(df_with_prefix)
