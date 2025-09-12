import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'A', 'B'],
    'Values': [10, 20, np.nan, 30, 40, np.nan, 50]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
grouped = df.groupby('Category').apply(lambda x: x['Values'].dropna().std())

print(grouped)
