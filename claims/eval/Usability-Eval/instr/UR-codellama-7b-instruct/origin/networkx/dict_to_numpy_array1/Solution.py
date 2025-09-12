
import networkx as nx

# create a dictionary of numbers
numbers = {0: 3.14, 1: 2.7, 2: 1.61}

# convert the dictionary to a 1D numpy array
arr = nx.utils.dictionary_to_array(numbers)

print(arr)
