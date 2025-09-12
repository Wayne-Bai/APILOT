import pandas as pd

# Assuming df1 and df2 are your DataFrame objects
# If joining on index
df1.join(df2, how='inner')  # 'inner' is the default, you can use 'outer', 'left', 'right'

# If joining on a key column
df1.merge(df2, on='key_column', how='inner')

# Joining multiple DataFrame objects by index at once
dfs = [df1, df2, df3]  # replace df1, df2, df3 with your DataFrame objects
result = pd.concat(dfs, axis=1, join='inner')  # 'inner' is the default, you can use 'outer', 'left', 'right'
