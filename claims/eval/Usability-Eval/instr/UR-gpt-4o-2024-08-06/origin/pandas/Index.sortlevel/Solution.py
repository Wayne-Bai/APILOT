import pandas as pd

# Create a sample Index
index = pd.Index(['c', 'a', 'b', 'd'])

# Sort the Index
sorted_index = index.sort_values()

print(sorted_index)
