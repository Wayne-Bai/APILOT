import pandas as pd

# create a sample index
idx = pd.Index([1, 2, 3, 4])

# sort the index in ascending order
sorted_idx = idx.sort_values()

print(sorted_idx)
