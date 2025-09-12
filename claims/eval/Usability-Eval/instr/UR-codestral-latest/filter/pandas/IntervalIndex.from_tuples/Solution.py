import pandas as pd

# Array-like of tuples, where each tuple represents an interval
intervals = [(1, 3), (4, 6), (7, 9)]

# Construct IntervalIndex
idx = pd.IntervalIndex.from_tuples(intervals)

# Print the IntervalIndex
print(idx)
