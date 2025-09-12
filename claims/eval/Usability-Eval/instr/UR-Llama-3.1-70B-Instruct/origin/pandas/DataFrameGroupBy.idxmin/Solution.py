import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [4, np.nan, 2, 6, 5],
    'B': [np.nan, 7, 3, np.nan, 1],
    'C': [0, 2, 4, 0, 8]
})

def find_min_index(x):
    # Find the index of the minimum value
    return x.values.argmin()

# Apply the function to each row
min_index_rows = df.apply(find_min_index, axis=1)

# Apply the function to each column
min_index_cols = df.apply(find_min_index, axis=0)

print("Minimum Index Rows:\n", min_index_rows)
print("Minimum Index Columns:\n", min_index_cols)
