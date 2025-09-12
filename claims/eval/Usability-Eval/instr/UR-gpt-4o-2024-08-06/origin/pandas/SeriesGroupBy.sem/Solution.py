import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, np.nan, 25, 20, np.nan]
}

df = pd.DataFrame(data)

# Function to compute standard error of the mean, excluding missing values
def sem_without_na(x):
    # Remove missing values to calculate mean and count
    clean_x = x[~x.isnull()]
    if len(clean_x) > 0:
        return np.std(clean_x, ddof=1) / np.sqrt(len(clean_x))
    else:
        return np.nan

# Grouping by 'Group' and calculating the SEM
result = df.groupby('Group')['Value'].agg(sem_without_na)

print(result)
