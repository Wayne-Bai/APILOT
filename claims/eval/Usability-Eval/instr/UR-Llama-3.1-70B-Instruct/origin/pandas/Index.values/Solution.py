# Import the pandas library
import pandas as pd

# Create a pandas index
data_index = pd.Index(['apple', 'banana', 'cherry', 'date', 'elderberry'])

# Return an array representing the data in the Index
data_array = data_index.array

print(data_array)
