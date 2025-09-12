import pandas as pd

# Sample DataFrame
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C', None],
    'values': [10, 20, None, 30, 50, None, 40]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
variance_by_group = df.groupby('group')['values'].var(dropna=True)

print(variance_by_group)
