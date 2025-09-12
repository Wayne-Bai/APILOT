import pandas as pd

# Sample DataFrame
data = {
    'A': [10, 20, 30, 40],
    'Group': ['X', 'X', 'Y', 'Y']
}
df = pd.DataFrame(data)

# Grouping by 'Group' and computing the product of values in 'A' for each group
df['Product'] = df.groupby('Group')['A'].transform(lambda x: x.prod())

print(df)
