import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)

# Compute the average degree connectivity
average_degree_connectivity = nx.average_neighbor_degree(G)

print(average_degree_connectivity)
