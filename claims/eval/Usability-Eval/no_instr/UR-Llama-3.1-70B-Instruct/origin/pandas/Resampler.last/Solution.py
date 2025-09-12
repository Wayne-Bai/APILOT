import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, np.nan, np.nan, np.nan]
})

# Compute the last non-null entry of each column
last_non_null_entries = df.apply(lambda x: x.dropna().iloc[-1])

print(last_non_null_entries)
