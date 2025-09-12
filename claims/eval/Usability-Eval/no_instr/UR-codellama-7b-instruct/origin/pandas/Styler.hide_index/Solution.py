
import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

# set the index to be hidden
df.index.visible = False

# print the dataframe without the index
print(df)
