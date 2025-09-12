
import pandas as pd

# create a sample DataFrame
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'values': [1, 2, 3, None, 5, 6]}
df = pd.DataFrame(data)

# compute variance of groups, excluding missing values
variance = df.groupby('group')['values'].apply(lambda x: x.dropna().var())
print(variance)
