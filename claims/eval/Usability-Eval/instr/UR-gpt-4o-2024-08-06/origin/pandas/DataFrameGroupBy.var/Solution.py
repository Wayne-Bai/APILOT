import pandas as pd

# Sample DataFrame
data = {'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'Value': [10, 20, None, 30, 40, 50, None]}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
grouped_variance = df.groupby('Group')['Value'].var()
print(grouped_variance)
