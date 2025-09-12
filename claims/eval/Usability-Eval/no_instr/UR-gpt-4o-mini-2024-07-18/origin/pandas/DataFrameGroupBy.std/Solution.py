import pandas as pd

# Sample DataFrame creation
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', None],
    'value': [10, 20, 30, None, 50, 60, None, 80]
}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('group')['value'].std(skipna=True)

print(std_dev)
