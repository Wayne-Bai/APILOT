import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', None],
    'Values': [10, 20, None, 25, 30, 30, None, 15]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['Values'].std(skipna=True)

print(std_dev)
