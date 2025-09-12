import pandas as pd

# Assuming you have an array-like of tuples
intervals = [(1, 3), (5, 7), (9, 11)]

# Construct an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_arrays(start=intervals[:, 0], end=intervals[:, 1], closed='both')

print(interval_index)
