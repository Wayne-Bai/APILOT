
import pandas as pd

# create a sample dataframe with a MultiIndex
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': [1, 2, 3],
                   'C': [4, 5, 6]})
df.index = pd.MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])

# sort the MultiIndex at level=0
sorted_df = df.sort_index(level=0)

print(sorted_df)
