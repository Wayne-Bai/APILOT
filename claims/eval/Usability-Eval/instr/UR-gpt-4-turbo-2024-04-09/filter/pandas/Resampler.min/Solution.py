import pandas as pd

# Sample data
data = {
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [10, 15, 5, 20, 25, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute the minimum value for each group
min_values = df.groupby('group')['value'].min()
print(min_values)
