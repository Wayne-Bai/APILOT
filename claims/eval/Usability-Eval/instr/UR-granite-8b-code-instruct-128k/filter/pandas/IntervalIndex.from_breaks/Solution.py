
import pandas as pd

# Example array of splits
splits = [0, 5, 10, 15]

# Construct IntervalIndex from splits
index = pd.IntervalIndex.from_arrays(splits[:-1], splits[1:])

print(index)
