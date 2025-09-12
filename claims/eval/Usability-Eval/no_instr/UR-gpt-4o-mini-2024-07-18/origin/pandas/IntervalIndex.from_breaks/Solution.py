import pandas as pd

# Define the array of splits
splits = [0, 1, 3, 5, 8]

# Construct an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Display the created IntervalIndex
print(interval_index)
