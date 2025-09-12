import pandas as pd

# create a sample index
idx = pd.Index(['a', 'b', 'c'])

# sort the index
idx_sorted = idx.sort_values()

print(idx_sorted)
