import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, None, 22, 30, None, 45]
}

df = pd.DataFrame(data)

# Compute variance for each group excluding missing values
group_variance = df.groupby('Group')['Value'].var()

# Display the result
print(group_variance)
