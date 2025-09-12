import pandas as pd

# Sample data creation
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, None, 15, 10, None, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute the standard deviation for each group, excluding missing values
group_std = df.groupby('Group')['Value'].std(skipna=True)

# Display the result
print(group_std)
