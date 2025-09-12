import pandas as pd

# Creating a simple index
idx = pd.Index([3, 1, 2, 4])

# Sorting the index
sorted_idx = idx.sort_values()

print("Original Index:")
print(idx)

print("\nSorted Index:")
print(sorted_idx)
