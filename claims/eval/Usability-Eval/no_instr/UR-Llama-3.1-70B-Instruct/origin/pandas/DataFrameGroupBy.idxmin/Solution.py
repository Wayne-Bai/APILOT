# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'A': [4, 1, None, 7, 5],
    'B': [2, 3, 4, None, 6],
    'C': [np.nan, 5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Use idxmin function to find index of first occurrence of minimum over requested axis (by default it's axis=0)
min_index_column = df.idxmin()

# Use idxmin function to find index of first occurrence of minimum over requested axis (by axis=1)
min_index_row = df.idxmin(axis=1)

# Print the results
print("Index of first occurrence of minimum for each column:")
print(min_index_column)
print("\nIndex of first occurrence of minimum for each row:")
print(min_index_row)
