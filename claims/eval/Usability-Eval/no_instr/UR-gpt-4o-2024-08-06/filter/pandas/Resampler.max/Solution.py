import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 15, 25, 5, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by the 'Group' column and compute the maximum 'Value' for each group
max_values = df.groupby('Group')['Value'].max().reset_index()

# Display the result
print(max_values)
