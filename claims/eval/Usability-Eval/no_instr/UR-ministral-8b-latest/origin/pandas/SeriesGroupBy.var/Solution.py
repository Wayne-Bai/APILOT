import pandas as pd

# Sample data
data = {
    'Group': ['A', 'B', 'A', 'B', 'A', 'B', 'A', None],
    'Value': [10, 20, None, 30, 40, 50, None, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Fill missing values with a placeholder so they don't affect calculations
df.fillna(0, inplace=True)

# Compute variance of each group
group_variance = df.groupby('Group')['Value'].var()

print(group_variance)
