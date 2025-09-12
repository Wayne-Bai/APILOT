import pandas as pd

# Sample DataFrame with a MultiIndex
index = pd.MultiIndex.from_tuples([('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')], names=['First', 'Second'])
columns = pd.MultiIndex.from_tuples([('C', '1'), ('C', '2'), ('D', '1'), ('D', '2')], names=['Third', 'Fourth'])
data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
df = pd.DataFrame(data, index=index, columns=columns)

# Pivot the 'Second' level of the index to become a new level in the columns
pivoted_df = df.unstack(level='Second')

print(pivoted_df)
