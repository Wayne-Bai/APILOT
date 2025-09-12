import pandas as pd

# Example DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['Index1', 'Index2'])
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)

# Reset the index, removing all levels
df_reset = df.reset_index()

# If you want to reset only specific levels, you can specify them
# For example, reset only 'Index2' level
df_reset_partial = df.reset_index(level='Index2')

print(df_reset)
print(df_reset_partial)
