import pandas as pd

# An array-like of tuples with start and end of intervals
interval_data = [(0, 1), (2, 3), (4, 5)]

# Construct an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_tuples(interval_data)

print(interval_index)
