
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# assign index to axis 0 (rows)
df.index = ['a', 'b', 'c']
