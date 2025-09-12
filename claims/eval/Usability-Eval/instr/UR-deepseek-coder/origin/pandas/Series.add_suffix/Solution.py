import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Suffix labels with string 'suffix'
df = df.add_suffix('_suffix')

print(df)
