import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'group_column' is the column by which you want to group
def compute_sem(group_data):
    return group_data.mean() / np.sqrt(len(group_data))

sem = df.dropna()\
    .groupby('group_column')\
    .apply(compute_sem)
