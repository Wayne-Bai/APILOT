import pandas as pd

# Example array of splits
splits = [0, 5, 10, 15, 20]

# Constructing IntervalIndex
interval_index = pd.IntervalIndex.from_breaks(splits, closed='left')

print(interval_index)
