import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the first occurrence of maximum
df = pd.DataFrame({
    'column_name': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
})

# Find the maximum value in the column
max_value = df['column_name'].max()

# Find the first occurrence of the maximum value
first_occurrence = df[df['column_name'] == max_value].index[0]

print(first_occurrence)
