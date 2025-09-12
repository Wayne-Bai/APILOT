import networkx as nx

# Create a sample graph
G = nx.Graph()
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 5), (2, 4)]
G.add_edges_from(edges)

# Compute the average degree connectivity of the graph
avg_degree_connectivity = nx.average_degree_connectivity(G)

# Output the average degree connectivity
print("Average Degree Connectivity:", avg_degree_connectivity)
