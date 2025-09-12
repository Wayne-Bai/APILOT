import pandas as pd

# Create an IntervalIndex from two arrays defining the left and right bounds
interval_index = pd.interval_range(left=left, right=right)

# Output the resulting IntervalIndex object
print(interval_index)
