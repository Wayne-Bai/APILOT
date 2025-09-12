
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'B', 'A'],
        'value': [1, 2, 3, None, 5, 6]}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev_by_group = df.groupby('group')['value'].agg(lambda x: x.dropna().std())

print(std_dev_by_group)
