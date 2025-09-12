import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, None, 20, 25, None]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
grouped_variance = df.groupby('Group')['Value'].var(ddof=0, skipna=True)

print(grouped_variance)
