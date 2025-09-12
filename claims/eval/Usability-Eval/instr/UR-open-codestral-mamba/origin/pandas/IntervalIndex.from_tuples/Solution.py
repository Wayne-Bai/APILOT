import pandas as pd

# Assuming we have an array-like of tuples
tuples = [(0, 1), (2, 3), (4, 5)]

# We can create an IntervalIndex from an array-like of tuples in this way
interval_index = pd.IntervalIndex.from_tuples(tuples)

# Or we can create an IntervalIndex from two array-like objects (starts and ends)
starts = [0, 2, 4]
ends = [1, 3, 5]
interval_index2 = pd.IntervalIndex.from_tuples(list(zip(starts, ends)))

print(interval_index)
print(interval_index2)
