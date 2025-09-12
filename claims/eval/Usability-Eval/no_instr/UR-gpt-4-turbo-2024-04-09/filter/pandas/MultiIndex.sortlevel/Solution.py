import pandas as pd

# Example DataFrame with a MultiIndex
arrays = [
    ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    ['one', 'two', 'three', 'one', 'two', 'three']
]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
data = {'A': [1, 2, 3, 4, 5, 6], 'B': [7, 8, 9, 10, 11, 12]}
df = pd.DataFrame(data, index=index)

# Sorting the MultiIndex at a specific level
# Here, sorting by the second level which is 'second'
sorted_df = df.sort_index(level='second')

print(sorted_df)
