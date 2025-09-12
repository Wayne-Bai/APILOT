import pandas as pd

# Sample data creation with MultiIndex
arrays = [
    ['A', 'A', 'B', 'B'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
data = {'value': [1, 2, 3, 4]}
df = pd.DataFrame(data, index=index)

# Sorting MultiIndex at the 'number' level while respecting the original ordering
sorted_df = df.sort_index(level='number', sort_remaining=False)

print(sorted_df)
