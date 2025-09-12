import pandas as pd

# Example input data
interval_tuples = [(0, 1), (2, 3), (4, 5)]

# Create an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_arrays(interval_tuples)
