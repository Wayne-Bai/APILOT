import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

# Compute the extreme distance metric
extreme_distance = nx.extreme_distance(G)

# Print the result
print("The extreme distance metric of the graph is:", extreme_distance)
