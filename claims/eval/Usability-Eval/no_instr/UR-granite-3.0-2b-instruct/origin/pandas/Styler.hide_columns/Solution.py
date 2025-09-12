import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to hide
df = df.rename(columns={'column_name': 'new_column_name'})
