import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the minimum in
min_index = df['column_name'].idxmin()

print(min_index)
