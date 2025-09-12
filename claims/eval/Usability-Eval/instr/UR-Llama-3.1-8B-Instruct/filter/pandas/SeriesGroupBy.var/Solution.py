# Importing the pandas library
import pandas as pd
import numpy as np

# Creating a sample DataFrame with missing values
data = {
    'Group': ['A', 'B', 'A', 'B', 'A', np.nan, 'B', 'B', 'A', np.nan],
    'Value': [10, 15, 12, 18, 15, np.nan, 18, 22, 16, 20]
}
df = pd.DataFrame(data)

# Replace missing values with 0 (you can also use df.dropna() if needed)
df['Value'] = df['Value'].replace(np.nan, 0)

# Grouping by 'Group' and computing variance
variance = df.groupby('Group')['Value'].var()

# Printing the result
print(variance)
