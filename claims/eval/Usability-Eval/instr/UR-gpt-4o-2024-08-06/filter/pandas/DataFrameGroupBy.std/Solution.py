import pandas as pd
import numpy as np

# Sample data creation
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D'],
    'Values': [10, 20, np.nan, 15, 35, np.nan, 40, 50]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute standard deviation for each group, excluding missing values
group_std_dev = df.groupby('Group')['Values'].std()

print(group_std_dev)
