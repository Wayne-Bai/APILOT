import pandas as pd

# Assuming that df1 and df2 are the DataFrames you want to join
# df1 and df2 are DataFrame objects

# To join DataFrames based on index, you can use the join method
# Combining df1 and df2 based on index
df_joined = df1.join(df2, how='inner')

# To join DataFrames based on a key column, you can use the merge method
# Combining df1 and df2 based on a key column
df_merged = pd.merge(df1, df2, on='key_column', how='inner')
