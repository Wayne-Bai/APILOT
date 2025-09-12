import pandas as pd

# Create a sample array of splits
splits = [0, 5, 10, 15, 20]

# Create an IntervalIndex from the array of splits
index = pd.IntervalIndex.from_arrays(splits, closed='both')

print(index)
