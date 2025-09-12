import pandas as pd

# Create a Series
data = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")
print(data)

# Prefix the label of the Series
prefixed_series = data.add_prefix('S_')
print("\nSeries with prefixed labels:")
print(prefixed_series)

# Create a DataFrame
data_dict = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}
df = pd.DataFrame(data_dict)
print("\nOriginal DataFrame:")
print(df)

# Prefix the column labels of the DataFrame
prefixed_df = df.add_prefix('Col_')
print("\nDataFrame with prefixed column labels:")
print(prefixed_df)
