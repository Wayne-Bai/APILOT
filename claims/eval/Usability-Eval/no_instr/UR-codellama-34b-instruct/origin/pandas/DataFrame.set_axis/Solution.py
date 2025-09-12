
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# set the index for axis 0 (rows) to be the values in column A
df.set_index('A', inplace=True)
