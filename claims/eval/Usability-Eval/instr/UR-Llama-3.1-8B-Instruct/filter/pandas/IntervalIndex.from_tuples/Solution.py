import pandas as pd

# Constructing an array-like of tuples
tuple_array = [(1, 5), (10, 15), (20, 25)]

# Creating an IntervalIndex from the tuple array
interval_index = pd.IntervalIndex(tuple_array, closed='both')

# Print IntervalIndex
print(interval_index)
