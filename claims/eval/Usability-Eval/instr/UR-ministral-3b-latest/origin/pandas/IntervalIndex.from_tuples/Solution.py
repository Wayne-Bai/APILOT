import pandas as pd

# Assuming the input array-like of tuples
tuples_array = [(1, 2), (3, 4), (5, 6)]

# Create an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_tuples(tuples_array, closed='both')

# Print the IntervalIndex
print(interval_index)
