import pandas as pd

# For Series
def prefix_labels_series(series, prefix):
    series.index = prefix + series.index
    return series

# For DataFrame
def prefix_labels_dataframe(df, prefix):
    df.columns = prefix + df.columns
    return df
