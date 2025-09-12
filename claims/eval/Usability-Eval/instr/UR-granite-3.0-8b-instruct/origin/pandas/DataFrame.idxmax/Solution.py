import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the first occurrence of the maximum value in
df = pd.DataFrame({'column_name': [1, 2, 3, 4, 5]})

# Find the maximum value in the column
max_value = df['column_name'].max()

# Find the index of the first occurrence of the maximum value
index = df[df['column_name'] == max_value].index[0]

index
