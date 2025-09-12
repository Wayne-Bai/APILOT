import pandas as pd

# Assuming the array-like of tuples is as follows
tuples = [(1, 3), (5, 7), (10, 12), (15, 17)]

# Construct an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_tuples(tuples)

print(interval_index)
