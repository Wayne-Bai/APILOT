import pandas as pd

# Sample data for creating a DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Assign desired index to the given axis (rows in this case)
desired_index = ['one', 'two', 'three', 'four']
df.index = desired_index

# Assign desired column names to axis 1 if needed
desired_columns = ['Column1', 'Column2', 'Column3']
df.columns = desired_columns

# Display the updated DataFrame
print(df)
