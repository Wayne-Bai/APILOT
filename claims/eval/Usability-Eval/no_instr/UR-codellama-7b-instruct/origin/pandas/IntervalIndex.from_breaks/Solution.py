
import pandas as pd

# Example array of splits
splits = [[0, 2], [3, 5], [6, 8]]

# Create an IntervalIndex from the array of splits
index = pd.IntervalIndex.from_tuples(splits)

print(index)
