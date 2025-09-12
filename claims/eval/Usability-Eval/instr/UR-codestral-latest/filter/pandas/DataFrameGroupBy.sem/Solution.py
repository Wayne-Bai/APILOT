import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'group_column' is the column you want to group by

# Calculate the mean for each group
grouped_mean = df.groupby('group_column').mean()

# Calculate the standard deviation for each group
grouped_std = df.groupby('group_column').std()

# Calculate the count for each group
grouped_count = df.groupby('group_column').count()

# Calculate the standard error of the mean for each group
standard_error_of_mean = grouped_std / np.sqrt(grouped_count)
