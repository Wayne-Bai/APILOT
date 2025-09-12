import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the minimum value in
df = pd.DataFrame({'column_name': [5, 3, 1, 4, 2]})

# Drop NA/null values
df = df.dropna()

# Find the minimum value and its index
min_value = df['column_name'].min()
min_index = df['column_name'].idxmin()

print(f"Minimum value: {min_value}, Index: {min_index}")
