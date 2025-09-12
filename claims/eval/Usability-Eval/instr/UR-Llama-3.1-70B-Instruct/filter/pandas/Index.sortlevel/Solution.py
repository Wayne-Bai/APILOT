import pandas as pd
import numpy as np

# Generate a random Index
np.random.seed(0)
index = pd.Index(np.random.choice(10, size=10, replace=True))

# Print the original Index
print("Original Index:")
print(index)

# Sort the Index
sorted_index = index.sort_values()

# Print the sorted Index
print("\nSorted Index:")
print(sorted_index)
