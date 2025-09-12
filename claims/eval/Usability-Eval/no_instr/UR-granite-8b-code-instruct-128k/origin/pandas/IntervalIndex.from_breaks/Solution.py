import pandas as pd

# Define an array of splits
splits = [1, 3, 5, 7, 9]

# Create an IntervalIndex from the splits
index = pd.IntervalIndex.from_arrays(splits[:-1], splits[1:])

print(index)
