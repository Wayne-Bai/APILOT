import pandas as pd

# Assuming you have a DataFrame called 'df' and you want to find the index of the first occurrence of the minimum value in a specific column

min_index = df['column_name'].idxmin()

print(min_index)
