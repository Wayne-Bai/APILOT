import pandas as pd

# Example DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [1, 2, None, 4, 5, None]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
group_variance = df.groupby('Group')['Values'].var()

print(group_variance)
