import pandas as pd

# Example DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['Letter', 'Number'])
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)

# Reset the index
df_reset = df.reset_index()

# If you want to reset only specific levels of the MultiIndex
# df_reset_specific = df.reset_index(level='Number')

print(df_reset)
