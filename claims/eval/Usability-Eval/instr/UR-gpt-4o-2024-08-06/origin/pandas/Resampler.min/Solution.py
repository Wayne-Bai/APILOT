import pandas as pd

# Example DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 5, 15, 25, 10]
}

df = pd.DataFrame(data)

# Computing the minimum value for each group
min_values = df.groupby('Group')['Value'].min().reset_index()

print(min_values)
