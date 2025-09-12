import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute the sum of group values
grouped_sum = df.groupby('Group')['Value'].sum().reset_index()

print(grouped_sum)
