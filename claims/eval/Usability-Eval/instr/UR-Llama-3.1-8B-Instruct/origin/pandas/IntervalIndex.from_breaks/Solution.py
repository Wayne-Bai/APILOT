import pandas as pd

# Create an array of splits
splits = pd.Series([0, 5, 10, 15, 20])

# Create IntervalIndex from the splits array
intervals = pd.IntervalIndex.from_arrays(left=splits[:-1], right=splits[1:], closed='right')

# Print the IntervalIndex
print(intervals)
