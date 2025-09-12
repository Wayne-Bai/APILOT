# Import necessary libraries
import pandas as pd

# Create a pandas Series
series_data = ['apple', 'banana', 'cherry']
series = pd.Series(series_data, index=['fruit1', 'fruit2', 'fruit3'])

print("Original Series:")
print(series)

# Create another pandas Series with same length as original series
data_to_prefix = list(range(len(series)))
series_to_prefix = pd.Series(data_to_prefix, index=series.index)

# Prefix the original series labels with 'Fruit_'
series_prefix = series.map(lambda x: f"Fruit_{x}")

print("\nSeries after prefixing labels:")
print(series_prefix)

# Create a pandas DataFrame
data = {
    'A': ['apple', 'banana', 'cherry'],
    'B': ['date', 'elderberry', 'fig']
}
df = pd.DataFrame(data, index=['fruit1', 'fruit2', 'fruit3'])

print("\nOriginal DataFrame:")
print(df)

# Create another pandas DataFrame with same columns as original DataFrame
df_prefix_data = {
    'A': [1]*len(df),
    'B': [2]*len(df)
}
df_to_prefix = pd.DataFrame(df_prefix_data, index=df.index, columns=df.columns)

# Prefix the original DataFrame column labels with 'Column_'
df_prefix = df.rename(columns=lambda x: f"Column_{x}")

print("\nDataFrame after prefixing column labels:")
print(df_prefix)
