
import pandas as pd

# create a sample DataFrame with missing values
data = {'group': ['A', 'B', 'C', 'D', 'E'],
        'value': [1, 2, 3, np.nan, 5]}
df = pd.DataFrame(data)

# compute the variance of groups, excluding missing values
variance_groups = df.groupby('group')['value'].agg(['var'])

print(variance_groups)
