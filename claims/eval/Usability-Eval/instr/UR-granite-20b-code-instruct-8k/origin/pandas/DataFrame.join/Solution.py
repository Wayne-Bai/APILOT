import pandas as pd

# Assuming df1 and df2 are two DataFrames with columns 'A', 'B' and 'C'

# Joining on index
df3 = df1.join(df2, on=None, how='left', lsuffix='_df1', rsuffix='_df2', sort=False)

# Joining on key column
df4 = df1.join(df2, on='key_column', how='inner')
