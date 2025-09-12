import pandas as pd
import numpy as np

# Let's assume we have a dataframe df
df = pd.DataFrame({
    'Group': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'Value': [1, 2, np.nan, 4, 5, 6, 7, np.nan]
})

# We drop the rows with missing values
df = df.dropna()

# Then we use the groupby method to group by 'Group'
# and the std method to compute the standard deviation of 'Value'
std_dev = df.groupby('Group')['Value'].std()

# Now 'std_dev' is a series with the standard deviations of 'Value'
# for each group, excluding any missing values.
print(std_dev)
