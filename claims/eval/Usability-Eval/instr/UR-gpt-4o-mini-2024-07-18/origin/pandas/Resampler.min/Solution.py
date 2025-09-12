import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 5, 8, 12, 3, 7]
}

df = pd.DataFrame(data)

# Compute the minimum value for each group
min_values = df.groupby('Group')['Value'].agg('min').reset_index()

print(min_values)
