import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D', 'E'],
    'value2': [5, 6, 7, 8]
})

df3 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F'],
    'value3': [9, 10, 11, 12]
})

# Join DataFrames on 'key' column
merged_df = df1.merge(df2, on='key', how='outer')
merged_df = merged_df.merge(df3, on='key', how='outer')

# Alternatively, join multiple DataFrames by index at once
dfs = [df1, df2, df3]
merged_df_by_index = pd.concat(dfs, axis=1)

print(merged_df)
print(merged_df_by_index)
