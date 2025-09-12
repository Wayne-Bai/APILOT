# Importing the pandas library
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Value': [1, 2, np.nan, 4, 5, 6, np.nan]
}
df = pd.DataFrame(data)

# Computing variance of groups, excluding missing values
group_variance = df.groupby('Group')['Value'].var()

print(group_variance)
