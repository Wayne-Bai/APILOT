
import pandas as pd

# create a sample DataFrame with a MultiIndex
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'], 
                   'B': [1, 2, 3], 
                   'C': [4, 5, 6]}, 
                 index=[['a', 'b', 'c'], ['d', 'e', 'f']])

# reset the index of the DataFrame to its default value
df.reset_index(level=0)
