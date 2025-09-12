import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute the standard deviation for
std_dev = df['column_name'].dropna().std()

print("Standard Deviation:", std_dev)
