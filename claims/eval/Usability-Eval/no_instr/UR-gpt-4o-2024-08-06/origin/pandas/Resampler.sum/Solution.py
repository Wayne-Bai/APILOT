import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Compute sum of group values
group_sum = df.groupby('Group')['Value'].sum().reset_index()

print(group_sum)
