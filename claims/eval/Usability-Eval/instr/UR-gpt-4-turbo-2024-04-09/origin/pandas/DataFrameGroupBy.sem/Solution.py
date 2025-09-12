import pandas as pd

# Sample data creation
data = {'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Value': [20, 21, 22, 23, 24, None]}

df = pd.DataFrame(data)

# Compute standard error of the mean (SEM) for each group, excluding missing values
result = df.groupby('Group')['Value'].sem()

print(result)
