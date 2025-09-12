import pandas as pd

# Example array-like of tuples
tuples = [(1, 3), (4, 6), (7, 9)]

# Constructing IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(tuples, closed='left')

print(interval_index)
