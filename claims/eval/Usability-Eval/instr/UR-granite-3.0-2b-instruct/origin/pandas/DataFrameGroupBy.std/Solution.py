import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute standard deviation for
std_dev = df['column_name'].dropna().std()
