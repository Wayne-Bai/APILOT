import pandas as pd

# Array-like of tuples
tuples = [(1, 2), (3, 5), (6, 8)]

# Create IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(tuples)

print(interval_index)
