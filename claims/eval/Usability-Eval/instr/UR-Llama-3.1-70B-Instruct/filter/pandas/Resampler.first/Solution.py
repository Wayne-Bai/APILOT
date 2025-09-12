import pandas as pd
import numpy as np

# Create a DataFrame with null values
data = {
    'A': [np.nan, 1, np.nan, np.nan],
    'B': [np.nan, np.nan, 2, np.nan],
    'C': [np.nan, np.nan, np.nan, 3]
}
df = pd.DataFrame(data)

# Use the bfill method with axis=0 and limit=1 to get the first non-null entry of each column
first_non_null = df.bfill(axis=0).iloc[0]

print(first_non_null)
