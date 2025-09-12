import pandas as pd

# Create a sample Series
s = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
print("Original Series:")
print(s)

# Prefix the row labels with a string prefix
s_with_prefix = s.map(lambda x: f"{prefix}{x}")
print("\nSeries with Row Labels Prefixed:")
print(s_with_prefix)

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [40, 50, 60],
    'B': [70, 80, 90]
})
print("\nOriginal DataFrame:")
print(df)

# Prefix the column labels with a string prefix
df_with_prefix = df.rename(columns={col: prefix + col for col in df.columns})
print("\nDataFrame with Column Labels Prefixed:")
print(df_with_prefix)
