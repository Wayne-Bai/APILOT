import pandas as pd

# Assuming df is your DataFrame and you want to find the index of the first minimum value in the column 'column_name'
idx = df['column_name'].idxmin()
print(idx)
