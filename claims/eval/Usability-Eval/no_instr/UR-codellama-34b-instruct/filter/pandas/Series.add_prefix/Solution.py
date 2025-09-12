import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# prefix column names with 'column_'
prefix = 'column_'
df.columns = [prefix + col for col in df.columns]

print(df)
