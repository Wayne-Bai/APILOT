import pandas as pd

# Create an example Index
index = pd.Index([10, 22, 35, 47, 59])

# Return an array representing the data in the Index
index_array = index.array
print(index_array)
