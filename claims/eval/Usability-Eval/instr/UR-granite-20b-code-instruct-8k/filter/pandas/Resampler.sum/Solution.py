import pandas as pd
# create a dataframe
data = {'group': ['A', 'B', 'A', 'B', 'A'],
        'value': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
# compute sum of group values
result = df.groupby('group')['value'].sum()
print(result)
