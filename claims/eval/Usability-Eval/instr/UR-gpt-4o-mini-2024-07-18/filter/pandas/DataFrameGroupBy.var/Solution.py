import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', None],
    'Values': [10, 12, 20, 22, 30, None, None, 15]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
group_variance = df.groupby('Group')['Values'].var(ddof=0)  # ddof=0 for population variance
print(group_variance)
