import pandas as pd

# array of splits
splits = [0, 2, 5, 10]

# construct interval index
interval_index = pd.IntervalIndex.from_breaks(splits)
