import pandas as pd

# Assume df1 and df2 are two existing DataFrames
# Example DataFrames:
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [4, 5, 6]
})

# Joining df1 and df2 on key column
result = pd.merge(df1, df2, on='key', how='outer')

print(result)
