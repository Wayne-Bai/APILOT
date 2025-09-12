# Import the necessary library
import pandas as pd

# Define an array of splits
splits = [0, 1, 3, 5, 7, 9]

# Construct an IntervalIndex from the array of splits
index = pd.IntervalIndex.from_arrays(left=splits, right=splits[1:], closed='both')

# Print the IntervalIndex
print(index)
