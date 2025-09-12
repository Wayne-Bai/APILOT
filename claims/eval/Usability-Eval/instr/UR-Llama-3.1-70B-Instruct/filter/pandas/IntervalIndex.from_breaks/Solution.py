# Import the pandas library
import pandas as pd
import numpy as np

# Create an array of splits
splits = np.array([0, 3, 5, 7, 8, 10])

# Construct an IntervalIndex from the array of splits
index = pd.IntervalIndex.from_breaks(splits)

# Print the IntervalIndex
print(index)

# Alternatively, you can also construct IntervalIndex from an array of tuples (closed left, right)
# intervals = pd.IntervalIndex.from_tuples([(0, 3), (3, 5), (5, 7), (7, 8), (8, 10)], closed='left')

# Construct IntervalIndex from an array of integer arrays (left, right)
# intervals = pd.IntervalIndex.from_arrays([0, 3, 5, 7, 8], [3, 5, 7, 8, 10], closed='left')
