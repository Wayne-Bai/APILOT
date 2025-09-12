
import pandas as pd

# create a dictionary with the data for the multiindex dataframe
data = {('level1', 'level2'): [1, 2, 3], ('level1', 'level3'): [4, 5, 6]}

# create a MultiIndex DataFrame from the dictionary
df = pd.DataFrame(data)

# set the index levels as columns
df = df.reset_index()

print(df)
