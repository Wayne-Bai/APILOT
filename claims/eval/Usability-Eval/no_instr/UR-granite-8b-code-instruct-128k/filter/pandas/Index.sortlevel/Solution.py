
import pandas as pd

# Create a sample index
idx = pd.Index([3, 1, 2])

# Sort the index
sorted_idx = idx.sort_values()

# Print the sorted index
print(sorted_idx)
