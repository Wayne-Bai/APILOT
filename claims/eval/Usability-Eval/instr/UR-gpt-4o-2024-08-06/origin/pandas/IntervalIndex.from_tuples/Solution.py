import pandas as pd

# Array-like of tuples representing the intervals
data = [(0, 2), (3, 5), (6, 8), (9, 11)]

# Create the IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_tuples(data)

# Output the IntervalIndex
print(interval_index)
