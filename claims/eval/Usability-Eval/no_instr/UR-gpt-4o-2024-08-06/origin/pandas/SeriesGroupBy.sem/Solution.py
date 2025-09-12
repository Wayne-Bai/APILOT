import pandas as pd
import numpy as np

# Sample data
data = {
    'Group': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, np.nan, 30, 40, 50, np.nan]
}

df = pd.DataFrame(data)

# Function to calculate the standard error of the mean
def standard_error(x):
    return x.std(ddof=1) / np.sqrt(x.count())

# Group by 'Group' column and calculate the standard error for each group
result = df.groupby('Group')['Value'].apply(standard_error)
print(result)
