
import pandas as pd
data = {'A': ['foo', 'bar', 'baz'],
        'B': ['a', 'b', 'c'],
        'C': ['d', 'e', 'f']}
index = pd.MultiIndex.from_tuples([(1, 2), (3, 4), (5, 6)], names=['first', 'second'])
df = pd.DataFrame(data, index=index)
df.columns.names = ['level1', 'level2']
print(df)
