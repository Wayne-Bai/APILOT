import pandas as pd

# Create an array-like of tuples
intervals = [(0, 1), (1, 2), (2, 3), (3, 4)]

# Construct an IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(intervals)

# Display the IntervalIndex
print(interval_index)
