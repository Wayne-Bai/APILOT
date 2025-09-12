import pandas as pd

def prefix_labels_with_string(data, prefix):
    if isinstance(data, pd.Series):
        data.index = data.index.map(lambda x: f"{prefix}{x}")
    elif isinstance(data, pd.DataFrame):
        data.columns = data.columns.map(lambda x: f"{prefix}{x}")
    return data

# Example usage:
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("Original Series:")
print(series)

prefixed_series = prefix_labels_with_string(series, "prefix_")
print("\nPrefixed Series:")
print(prefixed_series)

dataframe = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
print("\nOriginal DataFrame:")
print(dataframe)

prefixed_dataframe = prefix_labels_with_string(dataframe, "prefix_")
print("\nPrefixed DataFrame:")
print(prefixed_dataframe)
