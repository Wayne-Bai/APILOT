import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to suffix
df['column_name'] = df['column_name'].str.strip().str.upper() + '_SUFFIX'
