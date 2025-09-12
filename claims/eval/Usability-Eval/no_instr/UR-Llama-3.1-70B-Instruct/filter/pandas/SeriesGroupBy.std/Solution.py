# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame with random data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, np.nan, 40, 50, np.nan, 70, 80]
}
df = pd.DataFrame(data)

# Compute standard deviation of groups, excluding missing values
std_dev_group = df.groupby('Category')['Value'].std(skipna=True)

print(std_dev_group)
