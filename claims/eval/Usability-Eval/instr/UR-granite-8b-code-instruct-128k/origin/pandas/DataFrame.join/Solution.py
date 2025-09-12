
import pandas as pd

# Assuming you have two DataFrames, df1 and df2
# You can join columns from df2 to df1 on the index using the following code:
df1 = pd.merge(df1, df2, how='left', left_index=True, right_index=True)

# You can also join columns from df2 to df1 on a specific key column using the following code:
df1 = pd.merge(df1, df2, how='left', on='key_column')

# Note: The 'left' parameter in the code specifies that we want to keep all rows from df1, and only add matching rows from df2.
# If you want to keep all rows from df2, and only add matching rows from df1, you can use 'right' instead.

