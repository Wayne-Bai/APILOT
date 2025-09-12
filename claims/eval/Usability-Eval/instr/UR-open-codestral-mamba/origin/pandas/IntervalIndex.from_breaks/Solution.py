import pandas as pd

# Assume we have an array of splits like this
array_of_splits = [0, 100, 200, 300, 400, 500]

# We can create a pandas Series with a custom index using IntervalIndex
series = pd.Series([0, 1, 2, 3, 4, 5], index=pd.IntervalIndex.from_breaks(array_of_splits))

print(series)
