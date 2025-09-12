import pandas as pd

# Create example DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'A', 'E'],
    'value': [5, 6, 7, 8]
})

# Joining df1 and df2 on key column
result = pd.merge(df1, df2, on='key', how='outer', suffixes=('_df1', '_df2'))

print(result)
