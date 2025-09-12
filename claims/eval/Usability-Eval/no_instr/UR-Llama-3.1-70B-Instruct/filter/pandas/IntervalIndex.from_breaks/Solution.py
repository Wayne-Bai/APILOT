# Import pandas library
import pandas as pd

# Construct an IntervalIndex from an array of splits
splits = [0, 5, 10, 15, 20]
index = pd.IntervalIndex.from_breaks(splits)

# Print the IntervalIndex
print(index)
