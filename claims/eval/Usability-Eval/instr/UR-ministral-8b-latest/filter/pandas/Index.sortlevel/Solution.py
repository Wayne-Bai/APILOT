import pandas as pd

# Sample data as a MultiIndex DataFrame
arrays = [
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [10, 20, 10, 40, 20, 50, 30, 80]
]
index = pd.MultiIndex.from_arrays(arrays, names=(' letters', 'numbers', 'group', 'value'))
df = pd.DataFrame(index=index, data=100).reset_index()

# Sorting MultiIndex
df = df.sort_index()

print(df)
