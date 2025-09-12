import pandas as pd

# Construct array-like of tuples
tuples = [(1, 3), (5, 7), (9, 11)]

# Construct IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(tuples)

print(interval_index)
