import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Compute the max value of each group
max_values = df.groupby('Group')['Value'].max().reset_index()

print(max_values)
