import pandas as pd

# Create a sample dataframe
data = {'group': ['A', 'B', 'C'], 'value1': [1, 2, np.nan], 'value2': [3, 4, 5]}
df = pd.DataFrame(data)

# Compute the variance of each group while excluding missing values
variance = df.groupby('group').agg({'value1': lambda x: x.dropna().var(),
                                    'value2': lambda x: x.dropna().var()})
