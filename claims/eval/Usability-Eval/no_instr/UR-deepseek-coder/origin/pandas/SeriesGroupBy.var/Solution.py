import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, None, 20, 12, 25]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
grouped_variance = df.groupby('Group')['Value'].var(ddof=0)

print(grouped_variance)
