import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, None, 50, 60]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Compute variance for each group, excluding missing values
group_variance = df.groupby('Group')['Values'].var()
print(group_variance)
