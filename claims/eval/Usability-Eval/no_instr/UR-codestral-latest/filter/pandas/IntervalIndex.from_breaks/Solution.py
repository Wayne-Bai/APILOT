# Importing the pandas library
import pandas as pd

# defining an array of splits
splits = [0, 5, 10, 15, 20]

# Construct an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Print the IntervalIndex
print(interval_index)
