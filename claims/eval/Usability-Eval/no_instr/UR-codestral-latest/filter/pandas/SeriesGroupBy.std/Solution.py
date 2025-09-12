import pandas as pd

# Assuming df is your DataFrame and column is the one you want to compute standard deviation
df_grouped = df.groupby('group_column')['column'].std()
