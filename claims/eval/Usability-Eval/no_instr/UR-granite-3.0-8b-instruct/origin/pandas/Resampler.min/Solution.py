import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute the min value for
min_value = df.groupby('column_name')['column_name'].min()
