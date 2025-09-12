import pandas as pd
import numpy as np

# Define the left and right bounds
left_bounds = np.array([1, 2, 3, 4, 5])
right_bounds = np.array([6, 7, 8, 9, 10])

# Construct an IntervalIndex from the bounds
interval_index = pd.arrays.IntervalArray.from_arrays(left_bounds, right_bounds, closed='both')

# Create a pandas Series using the IntervalIndex
series = pd.Series(range(len(interval_index)), index=interval_index)

print(series)
