import pandas as pd
import numpy as np

# Create a multi-indexed DataFrame
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=list('ABCD'))

# Sort DataFrame based on the 'second' level
df = df.sort_values(by=['second'])
print(df)
