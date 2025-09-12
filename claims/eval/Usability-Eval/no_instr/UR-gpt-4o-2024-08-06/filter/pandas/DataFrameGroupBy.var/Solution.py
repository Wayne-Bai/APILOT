import pandas as pd
import numpy as np

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C', np.nan, 'C'],
    'Value': [10, np.nan, 20, 25, 30, np.nan, 40, 35, 45]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute variance for each group, excluding missing values
group_variance = df.groupby('Group')['Value'].var()

print(group_variance)
