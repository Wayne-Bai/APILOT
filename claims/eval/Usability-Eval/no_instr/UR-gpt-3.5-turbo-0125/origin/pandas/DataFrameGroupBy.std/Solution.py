
import pandas as pd

# Create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'B', 'A'],
        'values': [10, 15, 20, None, 25, 30]}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('group')['values'].std()

print(std_dev)
