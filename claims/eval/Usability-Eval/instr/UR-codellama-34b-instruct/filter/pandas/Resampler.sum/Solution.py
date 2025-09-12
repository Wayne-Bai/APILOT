
import pandas as pd

# create a sample dataframe
data = {'group': ['A', 'B', 'C'],
        'value': [10, 20, 30]}
df = pd.DataFrame(data)

# compute the sum of group values
result = df.groupby('group')['value'].sum()
print(result)
