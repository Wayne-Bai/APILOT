import pandas as pd

# Create a list of tuples
intervals = [(1, 3), (4, 6), (7, 9)]

# Construct an IntervalIndex from the list of tuples
index = pd.IntervalIndex.from_tuples(intervals)

# Print the IntervalIndex
print(index)
