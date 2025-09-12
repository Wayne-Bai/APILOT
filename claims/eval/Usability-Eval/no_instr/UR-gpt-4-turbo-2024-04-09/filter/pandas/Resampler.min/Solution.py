import pandas as pd

# Sample DataFrame creation
data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 5, 3, 8, 7, 9]
}

df = pd.DataFrame(data)

# Compute the minimum value of each group
min_values = df.groupby('Group')['Value'].min()

print(min_values)
