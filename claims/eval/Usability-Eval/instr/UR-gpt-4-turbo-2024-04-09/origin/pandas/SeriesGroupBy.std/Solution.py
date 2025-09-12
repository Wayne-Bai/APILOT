import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [20, 21, 19, 18, 22, None]
}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
result = df.groupby('Group')['Values'].std()

print(result)
