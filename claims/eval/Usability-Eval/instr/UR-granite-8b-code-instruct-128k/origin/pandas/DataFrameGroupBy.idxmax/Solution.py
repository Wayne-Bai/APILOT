import pandas as pd

# Assuming you have a DataFrame named 'df' and you want to find the index of the first occurrence of the maximum value in a specific column
max_value = df['column_name'].max()
max_index = df['column_name'].idxmax()

print(f"The index of the first occurrence of the maximum value is: {max_index}")
