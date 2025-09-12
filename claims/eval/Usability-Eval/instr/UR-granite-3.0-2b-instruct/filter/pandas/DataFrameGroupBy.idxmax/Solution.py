import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the maximum in
max_value = df['column_name'].max()
max_index = df['column_name'].idxmax()

print(max_index)
