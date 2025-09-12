import pandas as pd
import numpy as np

# Sample data
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, np.nan, 8, 12, 18, 9, 11, 13]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute standard error of the mean of groups, excluding missing values
se = df.groupby('Group')['Value'].sem()

print(se)
