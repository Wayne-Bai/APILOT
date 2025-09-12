import pandas as pd

# Assuming df1 and df2 are your DataFrames
# Join on index
df1.join(df2)

# Join on a key column
df1.set_index('key_column').join(df2.set_index('key_column'))

# Join multiple DataFrames at once
dfs = [df1, df2, df3]  # replace df1, df2, df3 with your DataFrames
pd.concat(dfs, axis=1)
