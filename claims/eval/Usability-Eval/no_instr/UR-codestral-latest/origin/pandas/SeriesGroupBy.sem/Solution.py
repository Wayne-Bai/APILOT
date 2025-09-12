import pandas as pd
import numpy as np

# Assume you have a DataFrame df with columns 'group' and 'value'
# 'group' identifies each observation's group
# 'value' is the observation's value

# First, calculate the mean of each group, excluding NaN values
group_means = df.groupby('group')['value'].mean()

# Then, calculate the count of non-missing values in each group
group_counts = df.groupby('group')['value'].count()

# Then, calculate the standard deviation of each group, excluding NaN values
group_std = df.groupby('group')['value'].std()

# Finally, calculate the standard error of the mean
group_sem = group_std / np.sqrt(group_counts)

print(group_sem)
