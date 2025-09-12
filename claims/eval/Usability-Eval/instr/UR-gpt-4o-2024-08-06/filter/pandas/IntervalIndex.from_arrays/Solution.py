import pandas as pd

# Define the left and right bounds
left_bounds = [1, 3, 5, 7]
right_bounds = [2, 4, 6, 8]

# Construct a pandas IntervalIndex from the arrays
intervals = pd.IntervalIndex.from_arrays(left_bounds, right_bounds, closed='both')

# Display the intervals
print(intervals)
