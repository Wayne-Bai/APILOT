import networkx as nx
import numpy as np

# Example input data
input_data = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 3, 'C': 4},
    'C': {'A': 5, 'B': 6}
}

# Define the mapping function
def map_function(key):
    return key + '_mapped'

# Convert the dictionary of dictionaries to a 2D NumPy array with optional mapping
array = np.array([[input_data[key1][key2] for key2 in input_data[key1]] for key1 in input_data])
if map_function:
    array = array.applymap(lambda x: map_function(x))

# Print the result
print(array)
