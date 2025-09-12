import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 10, 20, 10, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute maximum value of each group
max_values = df.groupby('Group')['Value'].max()

print(max_values)
