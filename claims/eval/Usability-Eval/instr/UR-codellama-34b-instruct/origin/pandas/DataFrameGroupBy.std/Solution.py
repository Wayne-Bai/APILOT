import pandas as pd

# create a sample dataframe with numerical and non-numerical columns
data = {'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e'], 'C': [1.0, 2.0, 3.0, np.nan, 5.0]}
df = pd.DataFrame(data)

# compute standard deviation of groups, excluding missing values
std_dev = df.groupby(['A'])[['B', 'C']].agg({'B': lambda x: x.str.upper(), 'C': np.nanmean})
print(std_dev)
