import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute the product of values for each group
grouped = df.groupby('Group').agg({'Value': 'prod'}).reset_index()

print(grouped)
