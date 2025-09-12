import pandas as pd

# Example DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, None, 20, 25, None, 30]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
result = df.groupby('Group').std()
print(result)
