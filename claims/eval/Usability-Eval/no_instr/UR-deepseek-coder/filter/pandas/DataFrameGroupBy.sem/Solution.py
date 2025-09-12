import pandas as pd

# Sample data
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Value': [1, 2, None, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute the standard error of the mean for each group
grouped = df.groupby('Group')['Value'].agg(
    mean='mean',
    std='std',
    count='count'
).reset_index()

grouped['sem'] = grouped['std'] / grouped['count'].pow(0.5)

print(grouped[['Group', 'mean', 'sem']])
