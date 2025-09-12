import pandas as pd

# Sample DataFrame
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C', None],
    'value': [10, 20, 30, None, 50, 40, 60]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
group_variance = df.groupby('group')['value'].var()

print(group_variance)
