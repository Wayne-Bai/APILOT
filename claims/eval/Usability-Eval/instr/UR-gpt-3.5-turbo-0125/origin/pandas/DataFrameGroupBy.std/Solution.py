
import pandas as pd

# Sample data
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value': [1, 2, 3, None, 5, 6]}

df = pd.DataFrame(data)

# Function to compute standard deviation of groups, excluding missing values
def custom_std(group):
    return group.dropna().std()

grouped_std = df.groupby('group')['value'].agg(custom_std)

print(grouped_std)
