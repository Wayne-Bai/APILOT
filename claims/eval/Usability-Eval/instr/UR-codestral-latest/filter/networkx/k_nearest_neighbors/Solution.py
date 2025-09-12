import networkx as nx

# Create a graph for demonstration purposes
G = nx.path_graph(5)

# Compute the degree of each node
degrees = dict(G.degree())

# Compute the average degree connectivity
avg_degree_connectivity = sum(degrees.values()) / len(degrees)

print("Average degree connectivity:", avg_degree_connectivity)
