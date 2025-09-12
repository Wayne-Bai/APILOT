import pandas as pd

# Assuming this is your data
data = {
    'ID': [1, 2, 3, 4, 5],
    'A1': [10, 15, 20, 25, 30],
    'A2': [100, 150, 200, 250, 300],
    'B1': [5, 10, 15, 20, 25],
    'B2': [50, 100, 150, 200, 250],
    'C1': [1.1, 2.2, 3.3, 4.4, 5.5],
    'C2': [11.1, 22.2, 33.3, 44.4, 55.5]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Stack the levels, make 'ID' as the index and all the other columns into a multi-level index
stacked_df = df.set_index('ID').stack().reset_index()
stacked_df.columns = ['ID', 'Index', 'Value']

# Rename the columns
renamed_df = stacked_df.rename(columns={'Index': 'Level'})

print("\nDataframe with specified levels stacked:")
print(renamed_df)

# Optionally, pivot the DataFrame to convert 'Level' back to a column
pivoted_df = renamed_df.pivot(index='ID', columns='Level', values='Value').reset_index()
pivoted_df.columns = ['ID', 'A2', 'B2', 'C2']

print("\nPivoted DataFrame:")
print(pivoted_df)
