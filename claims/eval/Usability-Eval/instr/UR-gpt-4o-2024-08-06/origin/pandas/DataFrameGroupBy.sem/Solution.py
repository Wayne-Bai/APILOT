import pandas as pd
import numpy as np

# Sample data
data = {'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'Value': [10, np.nan, 20, 30, np.nan, 50, 70]}

# Create DataFrame
df = pd.DataFrame(data)

# Custom function to compute standard error of the mean
def standard_error(x):
    return x.std() / np.sqrt(len(x))

# Group by 'Group' and compute standard error of the mean excluding missing values
sem_grouped = df.groupby('Group')['Value'].agg(lambda x: standard_error(x.dropna()))

print(sem_grouped)
