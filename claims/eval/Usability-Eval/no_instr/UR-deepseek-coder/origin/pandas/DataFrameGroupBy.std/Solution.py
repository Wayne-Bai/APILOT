import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 20, 30, None, 40, 50]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('Group')['Value'].std(ddof=0)

print(std_dev)
