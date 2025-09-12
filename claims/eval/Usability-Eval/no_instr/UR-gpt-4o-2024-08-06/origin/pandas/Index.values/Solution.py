import pandas as pd

# Sample index creation
index = pd.Index([10, 20, 30, 40, 50])

# Convert the index to a numpy array
index_array = index.to_numpy()

print(index_array)
