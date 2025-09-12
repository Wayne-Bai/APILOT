import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the first occurrence of maximum
max_value = df['column_name'].max()
first_occurrence = df[df['column_name'] == max_value].index[0]

print(f"The first occurrence of the maximum value in the column is at index: {first_occurrence}")
