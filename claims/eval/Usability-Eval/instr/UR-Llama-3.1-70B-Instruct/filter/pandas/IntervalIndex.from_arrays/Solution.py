import pandas as pd
import numpy as np

# Define the left and right bounds as numpy arrays
left = np.array([1, 3, 5, 7])
right = np.array([2, 4, 6, 8])

# Construct IntervalIndex from two arrays defining the left and right bounds
interval_index = pd.IntervalIndex.from_breaks(np.concatenate(([left[0]], right, [right[-1]])))

# Create a DataFrame with the IntervalIndex
df = pd.DataFrame({'Interval': interval_index})

print(df)
