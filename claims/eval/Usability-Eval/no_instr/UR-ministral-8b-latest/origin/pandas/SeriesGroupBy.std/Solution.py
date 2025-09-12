import pandas as pd

# Sample DataFrame
data = {
    'Group': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [1, 2, None, 4, 3, None, 5, 6, None, 7]
}

df = pd.DataFrame(data)

# Group by 'Group' and compute standard deviation, excluding missing values
grouped = df.groupby('Group')['Values'].agg(['std', lambda x: x.replace(sum(x), sum(x)/x.count())])

print(grouped)
