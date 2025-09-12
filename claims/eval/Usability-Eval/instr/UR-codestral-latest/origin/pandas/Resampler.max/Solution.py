import pandas as pd

# Assuming 'df' is your DataFrame and 'group_column' is the column based on which you want to group the data
df.groupby('group_column').agg({'values_column': 'max'})
