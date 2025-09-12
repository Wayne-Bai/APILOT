import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, None, 50, 60, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
group_std = df.groupby('Group')['Values'].std()
print(group_std)
