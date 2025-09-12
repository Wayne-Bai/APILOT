import pandas as pd

# Sample data creation
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 25, 30, 45, 12, 35]
}

df = pd.DataFrame(data)

# Compute the max value for each group
max_values = df.groupby('Category')['Value'].max()

print(max_values)
