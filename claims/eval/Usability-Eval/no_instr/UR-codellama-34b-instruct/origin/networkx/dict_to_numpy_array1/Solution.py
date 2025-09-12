import numpy as np
import networkx as nx

# Create a sample dictionary
my_dict = {1: "a", 2: "b", 3: "c"}

# Convert the dictionary to a NetworkX graph
G = nx.from_dict(my_dict, create_using=nx.Graph)

# Optional: map the nodes in the graph to integers
G = nx.relabel_nodes(G, lambda x: x % 2 == 0)

# Convert the graph to a 1D NumPy array
arr = np.array(G.edges())

print(arr)
