# Import pandas
import pandas as pd
import numpy as np

# Assuming you have a DataFrame df with columns 'Group' and 'Values'
df = pd.DataFrame({
    'Group': ['A', 'B', 'A', 'B', 'A', 'B', np.nan],
    'Values': [1, 2, 3, 4, 5, np.nan, 7]
})

# Calculate standard deviation of 'Values' for each 'Group', excluding missing values
std_dev = df.groupby('Group')['Values'].std()

print(std_dev)
