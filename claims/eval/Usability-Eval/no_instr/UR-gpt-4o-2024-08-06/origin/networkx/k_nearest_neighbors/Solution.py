import networkx as nx

# Create a sample graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)])

# Compute the average degree connectivity of the graph
average_degree_connectivity = nx.average_degree_connectivity(G)

# Print the results
print("Average Degree Connectivity:")
for degree, avg_neighbor_degree in average_degree_connectivity.items():
    print(f"Degree {degree}: {avg_neighbor_degree:.2f}")
