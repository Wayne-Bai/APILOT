import pandas as pd

# Sample data creation
data = {
    'ID': [1, 2, 2, 3, 3, 3],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Computing sum of group values based on 'ID'
group_sum = df.groupby('ID')['Value'].sum()

print(group_sum)
