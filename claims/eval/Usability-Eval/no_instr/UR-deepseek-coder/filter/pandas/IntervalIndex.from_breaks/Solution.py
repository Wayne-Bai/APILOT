import pandas as pd

# Example array of splits
splits = [0, 5, 10, 15, 20]

# Constructing the IntervalIndex
interval_index = pd.IntervalIndex.from_breaks(splits)

print(interval_index)
