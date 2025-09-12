
import pandas as pd

# create a sample dataframe
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'], 
        'value1': [10, 20, 30, 40, 50, 60], 
        'value2': [7, 8, 9, 10, 11, 12]}
df = pd.DataFrame(data)

# compute variance of groups, excluding missing values
variance_groups = df.groupby('group')['value1'].var(skipna=True)
print(variance_groups)
