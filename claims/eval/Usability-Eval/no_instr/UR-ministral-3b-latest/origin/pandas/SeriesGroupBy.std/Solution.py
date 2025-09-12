import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'A', None, 'B', 'B', 'B'],
    'Values': [1, 2, 2, None, 4, 4, 4]
}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
result = df.groupby('Group')['Values'].std().replace(None, 0).rename('Standard Deviation')

print(result)
