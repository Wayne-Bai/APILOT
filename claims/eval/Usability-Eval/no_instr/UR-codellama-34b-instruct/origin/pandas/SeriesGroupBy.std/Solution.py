
import pandas as pd

# create sample data
data = {'group': ['A', 'B', 'C'], 'value': [10, 20, np.nan]}
df = pd.DataFrame(data)

# compute standard deviation of groups while excluding missing values
std_devs = df.groupby('group')['value'].agg(lambda x: x[~np.isnan(x)].std())
print(std_devs)
