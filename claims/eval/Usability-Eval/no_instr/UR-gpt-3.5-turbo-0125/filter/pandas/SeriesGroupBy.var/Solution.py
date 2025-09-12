
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
        'value': [3, 5, 7, None, 4, 10, 12]}
df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
variance_per_group = df.groupby('group')['value'].var()

print(variance_per_group)
