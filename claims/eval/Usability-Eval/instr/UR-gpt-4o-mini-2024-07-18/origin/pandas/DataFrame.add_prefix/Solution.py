import pandas as pd

# Example for Series
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
prefix_series = series.rename(lambda x: 'prefix_' + x, axis=0)

# Example for DataFrame
dataframe = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
prefix_dataframe = dataframe.rename(lambda x: 'prefix_' + x, axis=1)

print("Prefixed Series:")
print(prefix_series)
print("\nPrefixed DataFrame:")
print(prefix_dataframe)
