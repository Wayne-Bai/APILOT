
import numpy as np
import networkx as nx

# Sample dictionary of dictionaries
data = {
    'A': {'B': 1, 'C': 2, 'D': 3},
    'B': {'A': 1, 'C': 4, 'D': 5},
    'C': {'A': 2, 'B': 4, 'D': 6},
    'D': {'A': 3, 'B': 5, 'C': 6}
}

# Create a graph from the dictionary
G = nx.Graph(data)

# Extract the nodes and sort them
nodes = sorted(G.nodes())

# Create an empty numpy array
num_nodes = len(nodes)
adj_matrix = np.zeros((num_nodes, num_nodes))

# Fill the adjacency matrix
for node1_idx, node1 in enumerate(nodes):
    for node2_idx, node2 in enumerate(nodes):
        if node1 != node2:
            try:
                weight = G[node1][node2]['weight']
            except KeyError:
                weight = np.inf
            adj_matrix[node1_idx, node2_idx] = weight

print(adj_matrix)
