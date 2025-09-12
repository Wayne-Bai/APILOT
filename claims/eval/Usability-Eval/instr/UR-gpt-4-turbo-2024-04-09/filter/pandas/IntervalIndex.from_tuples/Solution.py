import pandas as pd

# Array-like of tuples representing the intervals
intervals = [(1, 2), (3, 5), (6, 8)]

# Constructing an IntervalIndex from an array-like of tuples
interval_index = pd.IntervalIndex.from_arrays([x[0] for x in intervals], [x[1] for x in intervals], closed='right')

print(interval_index)
