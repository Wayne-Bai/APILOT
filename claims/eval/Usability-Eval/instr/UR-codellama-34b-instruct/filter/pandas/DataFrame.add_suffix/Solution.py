import pandas as pd

# create a sample dataframe
data = {'A': ['apple', 'banana', 'cherry'], 'B': [1, 2, 3]}
df = pd.DataFrame(data)

# add a suffix to the labels of column A
df['A'] = df['A'].add_suffix('_new')

print(df)
