import pandas as pd

# Sample data to demonstrate
arrays = [
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo'],
    ['one', 'two', 'one', 'two', 'one', 'two'],
]

tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]}, index=index)

# Sorting the MultiIndex at the specified level
df_sorted = df.sort_index(level='first')

print(df_sorted)
