import pandas as pd

# create a sample dataframe
data = {'group': ['A', 'B', 'C'],
        'value': [10, 20, 30]}
df = pd.DataFrame(data)

# compute product of group values
prod = df.groupby('group')['value'].agg(pd.Series.product).rename('prod')
print(prod)
