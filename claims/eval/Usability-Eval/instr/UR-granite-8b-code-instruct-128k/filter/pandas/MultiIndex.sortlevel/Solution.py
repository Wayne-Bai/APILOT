import pandas as pd

# Create a MultiIndex
mi = pd.MultiIndex.from_product([['A', 'B'], ['C', 'D']])

# Sort the MultiIndex at level 0
sorted_mi = mi.sort_values(level=0)

print(sorted_mi)
