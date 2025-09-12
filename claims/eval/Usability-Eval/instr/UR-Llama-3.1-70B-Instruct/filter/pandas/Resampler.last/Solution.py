# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame with some null values
data = {
    'A': [1, 2, np.nan, np.nan, 5],
    'B': [np.nan, 'dogs', 'cats', np.nan, 'birds'],
    'C': [np.nan, np.nan, np.nan, 'Hello', np.nan],
    'D': [1.0, 2.0, np.nan, np.nan, np.nan]
}
df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null_entries = df.apply(lambda x: x.dropna().iloc[-1])

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Print the last non-null entry of each column
print("\nLast non-null entry of each column:")
print(last_non_null_entries)
