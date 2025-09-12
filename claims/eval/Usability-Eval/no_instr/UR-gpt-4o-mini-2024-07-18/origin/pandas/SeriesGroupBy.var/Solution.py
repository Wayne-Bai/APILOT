import pandas as pd

# Sample DataFrame
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C', None],
    'values': [10, 20, 30, None, 50, 60, 70]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
variance_per_group = df.groupby('group')['values'].var(skipna=True)

print(variance_per_group)
