import pandas as pd

# Creating an Index
index = pd.Index([2, 3, 5, 7, 11])

# Returning an array representing the data in the Index
array_from_index = index.to_numpy()
print(array_from_index)
