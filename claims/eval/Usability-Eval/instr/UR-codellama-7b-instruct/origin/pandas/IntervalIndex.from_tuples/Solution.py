
import pandas as pd

# Create a list of tuples
tuples = [(1, 3), (2, 4), (5, 6)]

# Convert the list of tuples to an IntervalIndex
index = pd.IntervalIndex(tuples)

print(index)
