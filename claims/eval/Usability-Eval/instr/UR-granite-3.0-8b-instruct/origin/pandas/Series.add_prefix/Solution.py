import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to prefix
df['column_name'] = 'prefix_' + df['column_name'].astype(str)
