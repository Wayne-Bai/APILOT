import pandas as pd

# Assuming 'splits' is your array of splits
splits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Construct an IntervalIndex from the array of splits
interval_index = pd.IntervalIndex.from_splits(splits, name='interval_index')

print(interval_index)
