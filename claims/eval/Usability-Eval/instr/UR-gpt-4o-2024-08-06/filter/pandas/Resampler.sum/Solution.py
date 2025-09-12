import pandas as pd

# Example DataFrame
data = {
    'Group': ['A', 'B', 'A', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Compute the sum of values for each group
grouped_sum = df.groupby('Group')['Value'].agg('sum').reset_index()

print(grouped_sum)
