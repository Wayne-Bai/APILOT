
import pandas as pd

# create a sample dataframe
data = {'group': ['A', 'B', 'C', 'A', 'B', 'C'],
        'value': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

# compute the maximum value in each group using groupby and transform
max_values = df.groupby('group')['value'].transform('max')
print(max_values)
