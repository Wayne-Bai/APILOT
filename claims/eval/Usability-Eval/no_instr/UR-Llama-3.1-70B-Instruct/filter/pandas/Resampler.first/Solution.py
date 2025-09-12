# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame with null values
data = {
    'A': [np.nan, 1, 2, 3],
    'B': [4, np.nan, 6, 7],
    'C': [np.nan, np.nan, np.nan, 10],
    'D': [11, 12, 13, 14]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.bfill().iloc[0]

print("Original DataFrame:")
print(df)

print("\nFirst non-null entry of each column:")
print(first_non_null)
