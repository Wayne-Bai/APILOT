
import pandas as pd

# Array of splits
splits = [0, 5, 10, 15]

# Constructing IntervalIndex from splits
interval_index = pd.IntervalIndex.from_breaks(splits)

print(interval_index)
