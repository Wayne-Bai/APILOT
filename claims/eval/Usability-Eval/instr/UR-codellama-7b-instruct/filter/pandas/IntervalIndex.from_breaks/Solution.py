
import pandas as pd

# construct an IntervalIndex from an array of splits
splits = [[1, 2], [3, 4], [5, 6]]
index = pd.IntervalIndex.from_arrays(splits)

print(index)
