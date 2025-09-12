import pandas as pd

# Sample dataframe
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Value': [1, 2, None, 3, None, 4, 5, 6, 7]
}
df = pd.DataFrame(data)

# Group by 'Group' and compute the standard deviation excluding missing values
std_dev_by_group = df.groupby('Group')['Value'].apply(lambda x: (x - x.mean()).std() if x.count() > 0 else None).reset_index(name='std_dev')

print(std_dev_by_group)
