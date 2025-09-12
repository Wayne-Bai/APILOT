
import pandas as pd

# create a sample dataframe with a MultiIndex
data = {'A': [10, 20, 30, 40, 50], 'B': [2, 4, 6, 8, 10]}
index = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z'), ('d', 'w'), ('e', 'v')], names=['level1', 'level2'])
df = pd.DataFrame(data, index)
print(df)

# sort the MultiIndex at level1
df.sort_values('level1', inplace=True)
print(df)
