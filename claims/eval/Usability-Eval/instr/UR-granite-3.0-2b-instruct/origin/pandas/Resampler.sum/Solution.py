import pandas as pd

# Assuming df is your DataFrame and 'group' is the column by which you want to group
total_sum = df.groupby('group').sum()
