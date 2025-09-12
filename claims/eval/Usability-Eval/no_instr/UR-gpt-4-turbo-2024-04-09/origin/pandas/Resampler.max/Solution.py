import pandas as pd

# Sample data frame
data = {
    'Group': ['A', 'B', 'A', 'B', 'C', 'C'],
    'Value': [20, 10, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Compute max value of each group
result = df.groupby('Group')['Value'].max()

print(result)
