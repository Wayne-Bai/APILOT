import pandas as pd

# create a sample DataFrame with missing values
df = pd.DataFrame({'group': ['A', 'B', 'C'],
                   'value': [10, 20, np.nan]})

# compute standard deviation of groups, excluding missing values
std_dev = df.groupby('group').agg(pd.NamedAgg(column='value', aggfunc=lambda x: x[~np.isnan(x)].std())).reset_index()

print(std_dev)
