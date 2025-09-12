import pandas as pd

# create a list of splits
splits = [0, 10, 20, 30, 40]

# convert the list to an IntervalIndex
interval_index = pd.IntervalIndex(splits)

print(interval_index)
