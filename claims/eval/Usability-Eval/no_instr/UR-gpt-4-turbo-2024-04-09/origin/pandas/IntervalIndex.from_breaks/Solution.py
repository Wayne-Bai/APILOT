import pandas as pd

# Define the array of split points
splits = [0, 1, 2, 3, 4, 5]

# Create an IntervalIndex from these splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Print the IntervalIndex
print(interval_index)
