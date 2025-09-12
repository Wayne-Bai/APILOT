import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

df3 = pd.DataFrame({
    'key': ['C', 'D', 'E'],
    'value3': [7, 8, 9]
})

# Joining multiple DataFrames on a key column
joined_df = pd.concat([df1, df2, df3], ignore_index=True)

print(joined_df)
