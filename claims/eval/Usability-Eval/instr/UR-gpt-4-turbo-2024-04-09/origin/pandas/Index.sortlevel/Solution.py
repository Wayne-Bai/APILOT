import pandas as pd

# Creating a sample Index
index = pd.Index([3, 1, 2, 5, 4])

# Sorting the Index
sorted_index = index.sort_values()

print(sorted_index)
