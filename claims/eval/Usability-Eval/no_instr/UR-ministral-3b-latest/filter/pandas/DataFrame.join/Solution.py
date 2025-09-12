import pandas as pd

# Assume df1 and df2 are two DataFrame objects

# To join on index
df3 = pd.DataFrame(df1.index, columns=['Index'])
df3 = pd.concat([df3, df1], axis=1)

# Reorder the columns if necessary
df3 = df3[[column for column in df1.columns if column != 'Index'] + ['Index']]

# Or to join on key column
df4 = df2.set_index('key_column')
result = df1.merge(df4, on='key_column', how='inner', indicator=True)
