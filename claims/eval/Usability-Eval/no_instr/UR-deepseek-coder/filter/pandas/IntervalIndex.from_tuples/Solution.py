import pandas as pd

# Example array-like of tuples
tuples = [(1, 3), (4, 6), (7, 10)]

# Constructing IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(tuples, closed='left')

print(interval_index)
