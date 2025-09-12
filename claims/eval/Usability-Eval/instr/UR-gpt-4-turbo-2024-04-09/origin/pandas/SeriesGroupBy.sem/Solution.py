import pandas as pd

# Creating a sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1.2, None, 2.5, 2.7, None, 3.1]
}

df = pd.DataFrame(data)

# Compute the standard error of the mean (SEM) for each group, excluding missing values
result = df.groupby('Group')['Value'].sem()

print(result)
