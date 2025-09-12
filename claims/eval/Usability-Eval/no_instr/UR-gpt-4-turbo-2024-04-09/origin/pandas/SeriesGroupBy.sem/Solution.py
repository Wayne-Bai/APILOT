import pandas as pd

# Create some sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, None, 15, 25, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group the data by 'Group' and compute the standard error of the mean, excluding missing values
result = df.groupby('Group')['Values'].sem()

print(result)
