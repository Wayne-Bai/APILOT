
# Importing the necessary libraries
import networkx as nx
import numpy as np

# Input dictionary of numbers
input_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# Mapping function (optional)
def map_function(value):
    return value * 2

# Creating a 1D numpy array from the dictionary values with optional mapping
values = np.array([map_function(input_dict[key]) for key in input_dict])

print(values)
