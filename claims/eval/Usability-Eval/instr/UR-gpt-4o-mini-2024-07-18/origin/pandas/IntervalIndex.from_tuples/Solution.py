import pandas as pd

# Create a list of tuples representing intervals
tuples = [(1, 3), (4, 6), (7, 9)]

# Construct an IntervalIndex from the list of tuples
interval_index = pd.IntervalIndex.from_breaks([start for start, end in tuples] + [end for start, end in tuples])

# Display the IntervalIndex
print(interval_index)
