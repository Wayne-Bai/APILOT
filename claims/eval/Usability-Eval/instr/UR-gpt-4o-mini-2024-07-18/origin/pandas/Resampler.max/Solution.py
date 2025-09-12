import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 15, 25, 30, 5]
}

df = pd.DataFrame(data)

# Compute max value of each group
max_values = df.groupby('Group')['Value'].agg('max').reset_index()

print(max_values)
