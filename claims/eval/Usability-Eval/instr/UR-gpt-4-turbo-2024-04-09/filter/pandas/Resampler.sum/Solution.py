import pandas as pd

# Sample data
data = {
    'Group': ['A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute sum of values grouped by 'Group'
grouped_sum = df.groupby('Group')['Value'].sum()
print(grouped_sum)
