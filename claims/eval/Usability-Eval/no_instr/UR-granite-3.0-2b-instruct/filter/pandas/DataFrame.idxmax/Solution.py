import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the index for
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

# Find the maximum value in the specified column
max_value = df['column_name'].max()

# Find the index of the first occurrence of the maximum value
index = df['column_name'].where(df['column_name'] == max_value).index[0]

print(index)
