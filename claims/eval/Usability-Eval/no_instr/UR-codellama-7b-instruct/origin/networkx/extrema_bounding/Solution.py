
import networkx as nx

# Define the graph G and compute its extreme distance metric
G = nx.Graph()
G.add_nodes_from([0, 1, 2])
G.add_edges_from([(0, 1), (0, 2), (1, 2)])

# Compute the extreme distance metric for G using Floyd-Warshall algorithm
metric = nx.floyd_warshall_shortest_path_length(G)

# Print the result
print("Extreme distance metric:", metric)
