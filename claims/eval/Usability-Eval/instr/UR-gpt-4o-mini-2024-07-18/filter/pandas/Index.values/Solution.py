import pandas as pd

# Example: Creating a pandas Index
index = pd.Index(['a', 'b', 'c', 'd', 'e'])

# Returning an array representing the data in the Index
index_array = index.to_numpy()

# Display the array
print(index_array)
