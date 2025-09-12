import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the minimum value in
df = pd.DataFrame({'column_name': [5, 2, 8, 1, 9, 3, 7]})
min_value = df['column_name'].min()

# Find the first occurrence of the minimum value
index = df[df['column_name'] == min_value].index[0]

print(index)
