import pandas as pd

# Assuming 'df' is your DataFrame and 'column_name' is the column to split
df['column_name'] = df['column_name'].str.split(',')
