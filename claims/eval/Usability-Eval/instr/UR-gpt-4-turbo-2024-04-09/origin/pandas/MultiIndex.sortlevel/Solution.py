import pandas as pd

# Create a sample DataFrame with MultiIndex
index = pd.MultiIndex.from_product([['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
                                   names=['first', 'second'])
df = pd.DataFrame({'A': range(8), 'B': range(8, 16)}, index=index)

# Sort the MultiIndex at level 'first'
sorted_df = df.sort_index(level='first')

print(sorted_df)
