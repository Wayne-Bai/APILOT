import pandas as pd

# Sample DataFrame creation
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, None, 30, 40, 50]
}

df = pd.DataFrame(data)

# Computing standard deviation of each group excluding missing values
grouped_std = df.groupby('Group')['Values'].std()
print(grouped_std)
