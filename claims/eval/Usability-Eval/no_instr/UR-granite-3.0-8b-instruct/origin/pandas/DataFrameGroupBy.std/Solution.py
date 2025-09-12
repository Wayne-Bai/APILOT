import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
df_grouped = df.dropna().groupby('group')

# Compute standard deviation of groups, excluding missing values
std_dev = df_grouped.std()
