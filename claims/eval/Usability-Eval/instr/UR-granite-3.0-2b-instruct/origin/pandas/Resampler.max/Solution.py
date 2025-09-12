import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column by which you want to group
max_value = df.groupby('column_name').max().max()
