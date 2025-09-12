import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'groupby_column1', 'groupby_column2', 'target_column' is your columns

df = pd.DataFrame({'groupby_column1': ['A']*3 + ['B']*2 + ['C']*1,
                   'groupby_column2': ['a']*2 + ['b']*2 + ['a']*2 + ['a']*1,
                   'target_column': [1, 2, np.nan, 4, 5, np.nan, 7]})

std_dev = df.groupby(['groupby_column1', 'groupby_column2'])['target_column'].std()
print(std_dev)
