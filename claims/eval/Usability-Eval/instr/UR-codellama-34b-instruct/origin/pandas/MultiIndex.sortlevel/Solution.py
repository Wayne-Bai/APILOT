
import pandas as pd

# create a sample MultiIndex DataFrame
df = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'qux'],
                   'B': ['one', 'two', 'three', 'four']})
df = df.set_index(['A', 'B'])

# sort the MultiIndex by the first level (i.e., "A")
sorted_df = df.sort_index(level=0)
print(sorted_df)
