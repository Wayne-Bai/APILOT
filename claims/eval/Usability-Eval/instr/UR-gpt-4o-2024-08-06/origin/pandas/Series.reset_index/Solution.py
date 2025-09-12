import pandas as pd

# Sample DataFrame
data = {'column1': [10, 20, 30], 'column2': [40, 50, 60]}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Resetting the index by creating a new DataFrame
df_reset_index = pd.DataFrame(df.values, columns=df.columns)
df_reset_index['index'] = range(len(df_reset_index))

# Optional: Set the 'index' as the DataFrame index
df_reset_index = df_reset_index.set_index('index')

print(df_reset_index)
