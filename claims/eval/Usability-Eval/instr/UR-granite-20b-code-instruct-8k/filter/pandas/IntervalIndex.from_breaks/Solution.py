import pandas as pd

# Define the array of splits
splits = [1, 3, 5, 7, 9]

# Create an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Print the IntervalIndex
print(interval_index)
