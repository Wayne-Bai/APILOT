import pandas as pd

# Define an array of split points
splits = [0, 5, 10, 15, 20]

# Construct the IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Display the IntervalIndex
print(interval_index)
