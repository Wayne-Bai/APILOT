import pandas as pd

# Create a sample Series
s = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")
print(s)

# Prefix labels with string prefix
s.name = "Prefixed_Series"
print("\nSeries with prefixed labels:")
print(s)

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print("\nOriginal DataFrame:")
print(df)

# Prefix column labels with string prefix
df.columns = ["Prefixed_A", "Prefixed_B"]
print("\nDataFrame with prefixed column labels:")
print(df)
