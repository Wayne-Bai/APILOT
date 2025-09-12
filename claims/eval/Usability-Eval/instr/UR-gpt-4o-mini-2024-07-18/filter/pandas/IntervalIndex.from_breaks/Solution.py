import pandas as pd

# Define the array of splits
splits = [0, 1, 2, 3, 4]  # Example splits

# Construct an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_breaks(splits)

# Display the IntervalIndex
print(interval_index)
