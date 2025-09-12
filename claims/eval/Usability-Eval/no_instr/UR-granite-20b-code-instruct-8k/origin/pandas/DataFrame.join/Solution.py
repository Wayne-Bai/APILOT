import pandas as pd

# Assuming df1 and df2 are two DataFrames to be joined
# Joining on index
df_joined = df1.join(df2, how='inner')

# Joining on key column
df_joined = df1.merge(df2, on='key_column', how='inner')
