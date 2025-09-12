import pandas as pd

# Create an array of splits
splits = ['2021-01-01', '2021-07-01', '2022-01-01']

# Convert the array of splits to a format suitable for pd.to_datetime
date_splits = pd.to_datetime(splits)

# Construct an IntervalIndex
interval_index = pd.IntervalIndex.from_tuples(date_splits)

# Display the IntervalIndex
print(interval_index)
