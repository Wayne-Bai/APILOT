
import pandas as pd

# create a sample dataframe with missing values
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value1': [1, 2, 3, 4, 5, 6],
        'value2': [np.nan, np.nan, 8, 9, 10, 11]}
df = pd.DataFrame(data)

# compute variance of groups excluding missing values using 'var' function
variance_excl_missing = df.groupby('group').var()
print(variance_excl_missing)
