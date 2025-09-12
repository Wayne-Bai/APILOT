import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add nodes and edges to your graph

# Compute the degree of each node
degree = nx.degree(G)

# Compute the average degree
avg_degree = sum(degree.values()) / len(degree)

# Compute the degree connectivity of each node
degree_connectivity = {k: [d for n, d in degree.items() if d == k] for k in set(degree.values())}

# Compute the average degree connectivity
avg_degree_connectivity = sum(len(v) / avg_degree for v in degree_connectivity.values()) / len(degree_connectivity)

print("Average degree:", avg_degree)
print("Average degree connectivity:", avg_degree_connectivity)
