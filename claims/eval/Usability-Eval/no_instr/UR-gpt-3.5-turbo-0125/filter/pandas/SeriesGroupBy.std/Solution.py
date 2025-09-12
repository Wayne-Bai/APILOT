
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'B', 'A'],
        'value': [1, 2, None, 4, 5, 6]}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('group')['value'].std()

print(std_dev)
