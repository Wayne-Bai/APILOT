import pandas as pd

# Example MultiIndex DataFrame
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8]}, index=index)

# Sort MultiIndex at the 'first' level
df_sorted = df.sort_index(level='first')

print(df_sorted)
