import pandas as pd

# create sample dataframe
data = {'group': ['A', 'B', 'C', 'D', 'E'],
        'value1': [2, 4, 6, 8, 10],
        'value2': [3, 5, 7, 9, 11]}
df = pd.DataFrame(data)

# compute variance of groups
variance = df.groupby('group').agg(lambda x: x.var())
print(variance)
