import pandas as pd

# Array of splits
splits = [0, 5, 10, 15, 20]

# Create the IntervalIndex from splits
interval_index = pd.IntervalIndex.from_breaks(splits)

print(interval_index)
