import pandas as pd

# Create a list of tuples
data = [(1, 2), (3, 4), (5, 6)]

# Create a pandas Series from the list of tuples
s = pd.Series(data)

# Construct an IntervalIndex from the Series
index = pd.IntervalIndex.from_tuples(s)

# Print the index
print(index)
