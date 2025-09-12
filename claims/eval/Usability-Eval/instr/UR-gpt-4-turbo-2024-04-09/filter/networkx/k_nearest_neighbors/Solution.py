import networkx as nx

# Create a graph
G = nx.gnp_random_graph(10, 0.5)

# Compute the average degree connectivity
avg_degree_connectivity = nx.average_degree_connectivity(G)

print("Average Degree Connectivity of the graph: ", avg_degree_connectivity)
