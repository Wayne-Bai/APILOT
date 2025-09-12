import pandas as pd

# Sample Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("Original Series:")
print(s)

prefix = "prefix_"
s.index = [prefix + label for label in s.index]
print("\nPrefixed Series:")
print(s)

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])
print("\nOriginal DataFrame:")
print(df)

df.columns = [prefix + col for col in df.columns]
print("\nPrefixed DataFrame:")
print(df)
