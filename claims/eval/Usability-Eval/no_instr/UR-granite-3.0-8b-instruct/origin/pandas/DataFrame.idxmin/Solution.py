import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the minimum value in
min_value = df['column_name'].min()

# Find the first occurrence of the minimum value
first_occurrence_index = df[df['column_name'] == min_value].index[0]

first_occurrence_index
