import pandas as pd

# Example DataFrame with a MultiIndex
arrays = [[1, 1, 2, 2], ['a', 'b', 'a', 'b']]
index = pd.MultiIndex.from_arrays(arrays, names=('number', 'letter'))
df = pd.DataFrame({'value': [10, 20, 30, 40]}, index=index)

# Reset the index
df_reset = df.reset_index()

# If you want to reset only one level of the MultiIndex, you can specify the level
# For example, to reset the 'letter' level
df_reset_level = df.reset_index(level='letter')

print(df_reset)
print(df_reset_level)
