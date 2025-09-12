import pandas as pd

# Example data
data = {'group': ['A', 'A', 'B', 'B', 'C'],
        'value': [10, 20, 30, 40, np.nan]}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_groups = df['value'].groupby(df['group']).transform('mean').std()
print(std_groups)
