import pandas as pd

# Sample DataFrame to demonstrate the functionality
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 15, 25, 30, 10, 20, 18]
}

df = pd.DataFrame(data)

# Compute min value of each group
min_values = df.groupby('Group')['Value'].min().reset_index()

print(min_values)
