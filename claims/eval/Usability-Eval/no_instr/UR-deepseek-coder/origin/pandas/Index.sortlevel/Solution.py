import pandas as pd

# Create an example Index
index = pd.Index([3, 1, 2, 5, 4])

# Sort the Index
sorted_index = index.sort_values()

print(sorted_index)
