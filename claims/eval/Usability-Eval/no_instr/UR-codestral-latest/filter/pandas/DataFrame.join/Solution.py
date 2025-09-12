import pandas as pd

# Suppose you have two dataframes df1 and df2
# df1
#    col1  col2
# 0      1     2
# 1      3     4

# df2
#    col3  col4
# 0      a     b
# 1      c     d

# join on index
df_join_index = df1.join(df2)

# or join on a key column 'key'
# suppose both dataframes have a common column 'key'
df_join_key = pd.merge(df1, df2, on='key')

# to join multiple dataframes at once
data_frames = [df1, df2, df3]  # list of dataframes to join
df_join_multiple = df1.join(data_frames)
