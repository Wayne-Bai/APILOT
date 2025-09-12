# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Group': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'Values': [1, 2, np.nan, 4, 5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
group_variance = df.groupby('Group')['Values'].var(skipna=True)

print(group_variance)
