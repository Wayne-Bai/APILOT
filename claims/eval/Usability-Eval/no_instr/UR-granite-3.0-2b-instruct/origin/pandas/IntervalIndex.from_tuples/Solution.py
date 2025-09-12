import pandas as pd

# Create a list of tuples
data = [(1, 2), (2, 3), (3, 4), (4, 5)]

# Create an IntervalIndex from the list of tuples
index = pd.IntervalIndex.from_tuples(data, name='my_index')

# Print the index
print(index)
