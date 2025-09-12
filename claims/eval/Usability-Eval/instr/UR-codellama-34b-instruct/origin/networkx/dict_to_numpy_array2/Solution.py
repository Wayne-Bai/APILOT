import networkx as nx

# Create a sample dictionary of dictionaries
sample_dict = {
    'A': {'a': 1, 'b': 2},
    'B': {'a': 3, 'c': 4},
    'C': {'b': 5, 'd': 6}
}

# Convert the dictionary of dictionaries to a 2D NumPy array
array = nx.to_numpy_matrix(sample_dict)

print(array)
