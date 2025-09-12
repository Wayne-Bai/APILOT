import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Compute shortest paths
path_lengths = nx.single_source_shortest_path_length(G, 1)

print("Shortest paths from node 1:", path_lengths)
