import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to split
df['split_column'] = df['column_name'].str.split('separator', expand=True)
