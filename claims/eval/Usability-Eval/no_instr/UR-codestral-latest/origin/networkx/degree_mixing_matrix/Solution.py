import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes with attributes
G.add_node(1, attribute=0.5)
G.add_node(2, attribute=0.8)
# Add more nodes as needed...

# Extract node attributes to a list
node_attributes = [G.nodes[n]['attribute'] for n in G]

# Create an adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

# Create the mixing matrix by multiplying the adjacency matrix with the diagonal matrix of attributes
mixing_matrix = np.diag(node_attributes) @ adj_matrix

print(mixing_matrix)
