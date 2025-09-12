import networkx as nx
import numpy as np

# Function to convert a dictionary of dictionaries to a 2D numpy array
def dict_of_dicts_to_2d_array(data, map_func=None):
    keys = list(data[0].keys())
    rows = [list(row.values()) for row in data]
    array = np.array(rows, dtype=np.float64)

    if map_func:
        def mapper(x):
            return map_func(x)

        array = np.vectorize(mapper)(array)

    return array

# Example usage
data = [
    {'A': 1.0, 'B': 2.0, 'C': 3.0},
    {'A': 4.0, 'B': 5.0, 'C': 6.0}
]

# Using the function with a mapping example (optional)
def square(x):
    return x ** 2

array = dict_of_dicts_to_2d_array(data, map_func=square)

print(array)
