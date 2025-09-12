import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, np.nan, 20, 30, 40, np.nan]
}

df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
grouped_std = df.groupby('Group')['Value'].std(skipna=True)

print(grouped_std)
