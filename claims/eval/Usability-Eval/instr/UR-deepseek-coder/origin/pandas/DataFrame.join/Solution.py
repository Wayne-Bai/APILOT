import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [4, 5, 6]
})

df3 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value3': [7, 8, 9]
})

# Join columns of another DataFrame on a key column
merged_df = df1.merge(df2, on='key', how='outer')
merged_df = merged_df.merge(df3, on='key', how='outer')

# Alternatively, join multiple DataFrames by index at once
dfs = [df1, df2, df3]
merged_df_by_index = pd.concat(dfs, axis=1)

print(merged_df)
print(merged_df_by_index)
