import pandas as pd

# Example array-like of tuples
tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Construct an IntervalIndex from the array-like of tuples
index = pd.IntervalIndex.from_tuples(tuples)

print(index)
