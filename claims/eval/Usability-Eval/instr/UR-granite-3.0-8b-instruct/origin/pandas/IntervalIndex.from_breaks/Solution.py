import pandas as pd

# Assuming you have an array of splits
splits = [0, 1, 2, 3, 4, 5]

# Create an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_splits(splits, name='interval_index')

# Print the IntervalIndex
print(interval_index)
