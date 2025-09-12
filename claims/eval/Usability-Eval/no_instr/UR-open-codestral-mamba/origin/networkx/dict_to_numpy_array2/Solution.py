import numpy as np
import networkx as nx

# Dictionary of dictionaries
data = {0: {1: 10, 2: 20}, 1: {0: 10, 2: 30}, 2: {0: 20, 1: 30}}

# Convert the dictionary of dictionaries to a networkx graph
G = nx.from_dict_of_dicts(data)

# Get the number of nodes in the graph
num_nodes = G.number_of_nodes()

# Initialize the numpy array with the correct shape
result = np.zeros((num_nodes, num_nodes), dtype=int)

# Fill the numpy array with the edge weights from the graph
for edge in G.edges(data=True):
    result[edge[0]][edge[1]] = edge[2]['weight']

result
