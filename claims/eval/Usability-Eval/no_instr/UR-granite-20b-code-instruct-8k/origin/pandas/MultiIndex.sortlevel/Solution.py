import pandas as pd
# Create a MultiIndex dataframe
index = pd.MultiIndex.from_tuples([(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd')], names=['level1', 'level2'])
df = pd.DataFrame({'data': range(4)}, index=index)
# Sort the MultiIndex at the 'level2' level while preserving the ordering of the associated factor at that level
sorted_df = df.sort_index(level='level2')
# Print the sorted dataframe
print(sorted_df)
