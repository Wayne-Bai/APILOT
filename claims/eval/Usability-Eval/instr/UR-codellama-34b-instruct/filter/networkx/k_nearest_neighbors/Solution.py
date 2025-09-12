import networkx as nx

# Create a sample graph
G = nx.gnp_random_graph(100, 0.5)

# Compute the average degree connectivity of the graph
avg_degree_connectivity = nx.average_degree_connectivity(G)

print("The average degree connectivity of the graph is:", avg_degree_connectivity)
