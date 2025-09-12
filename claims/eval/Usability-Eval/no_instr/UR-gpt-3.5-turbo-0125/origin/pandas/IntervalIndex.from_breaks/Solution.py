
import pandas as pd

# Defining the splits array
splits = [0, 5, 10, 15]

# Constructing IntervalIndex from splits array
interval_index = pd.IntervalIndex.from_breaks(splits)

print(interval_index)
