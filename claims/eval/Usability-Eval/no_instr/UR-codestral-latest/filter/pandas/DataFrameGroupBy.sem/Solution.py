# Import pandas library
import pandas as pd
import numpy as np

# Assuming df is your dataframe and 'group' is the column that contains the group information
def compute_sem(group_data):
    return group_data.mean() / np.sqrt(len(group_data))

# Drop missing values
df = df.dropna()

# Compute standard error of the mean for each group
sem_per_group = df.groupby('group').apply(compute_sem)
