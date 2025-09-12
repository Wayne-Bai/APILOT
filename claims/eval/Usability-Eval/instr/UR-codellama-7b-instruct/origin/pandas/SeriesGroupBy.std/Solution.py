
import pandas as pd

# create sample data
data = {'group': [1, 1, 2, 2, 3], 'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# compute standard deviation by group
df_std = df.groupby('group')['value'].agg(['mean', 'std'])
print(df_std)
