import pandas as pd
import numpy as np

# Example array of splits
splits = np.array([0, 3, 7, 10])

# Creating the IntervalIndex
interval_index = pd.IntervalIndex.from_breaks(splits)

print(interval_index)
