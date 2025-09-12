import pandas as pd

# Sample Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("Original Series:")
print(s)

# Prefix labels for Series
prefix = 'Label_'
s.index = [prefix + label for label in s.index]
print("\nSeries with prefixed labels:")
print(s)

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['d', 'e', 'f'])
print("\nOriginal DataFrame:")
print(df)

# Prefix labels for DataFrame
df.columns = [prefix + col for col in df.columns]
print("\nDataFrame with prefixed labels:")
print(df)
