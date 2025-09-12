
import pandas as pd

# create a sample dataframe
data = {'A': ['foo', 'bar', 'baz'], 'B': ['one', 'two', 'three']}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# pivot the level of the index labels
pivoted_df = df.pivot(index='A', columns='B')

print(pivoted_df)
