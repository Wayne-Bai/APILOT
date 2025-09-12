import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'Value': [4, np.nan, 6, 5, np.nan, 7, 8, 9]
}

df = pd.DataFrame(data)

# Group by 'Group' and compute the standard deviation, excluding missing values
std_deviation = df.groupby('Group')['Value'].std(skipna=True)

print(std_deviation)
