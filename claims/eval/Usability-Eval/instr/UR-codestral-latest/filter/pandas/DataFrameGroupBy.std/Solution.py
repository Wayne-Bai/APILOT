import pandas as pd

# Suppose 'df' is your DataFrame and 'group_col' is the column on which you want to group
# 'data_col' is the column for which you want to compute the standard deviation
grouped = df.dropna(subset=[data_col]).groupby(group_col)[data_col].std()
