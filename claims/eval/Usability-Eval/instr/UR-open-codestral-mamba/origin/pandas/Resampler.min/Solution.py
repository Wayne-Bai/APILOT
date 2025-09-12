import pandas as pd

# Assuming we have a DataFrame df with columns 'group' and 'value'
data = {'group': ['A', 'B', 'A', 'B', 'A'],
        'value': [5, 10, 7, 8, 3]}
df = pd.DataFrame(data)

# Compute min value of group
min_values = df.groupby('group')['value'].min()
print(min_values)
