import pandas as pd
import numpy as np

# Create a sample DataFrame with null values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, 2, 3, np.nan]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill null values with NaN (this is the default behavior)
df_filled = df.fillna(np.nan)

# Find the last non-null entry of each column
last_nonnull = df_filled.bfill().iloc[-1]

print("\nLast non-null entry of each column:")
print(last_nonnull)
