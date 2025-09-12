import pandas as pd

# Sample data
data = {
    'group': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'value': [10, None, 15, None, 20, 25, None, 30, 35]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
variance = df.groupby('group').apply(lambda x: x['value'].var())

# Display the result
print(variance)
