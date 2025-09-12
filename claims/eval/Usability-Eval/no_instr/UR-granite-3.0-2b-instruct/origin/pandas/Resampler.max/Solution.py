import pandas as pd

# Assuming df is your DataFrame and 'group' is the column based on which you want to group
max_value = df.groupby('group').max().max()
