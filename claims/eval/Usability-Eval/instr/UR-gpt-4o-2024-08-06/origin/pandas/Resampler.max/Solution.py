import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C'],
    'Value': [10, 15, 10, 25, 30, 5]
}

df = pd.DataFrame(data)

# Compute max value of each group
max_values = df.groupby('Group')['Value'].max()

print(max_values)
