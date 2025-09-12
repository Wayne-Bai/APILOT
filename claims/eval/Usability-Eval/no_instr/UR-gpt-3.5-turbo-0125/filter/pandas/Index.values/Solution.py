
import pandas as pd

# Creating a sample Index
index_data = pd.Index(['A', 'B', 'C', 'D', 'E'])

# Returning an array representing the data in the Index
index_array = index_data.values

print(index_array)
