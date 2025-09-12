import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Your code to create the graph goes here

# Compute the degree of each node
degree = nx.degree(G)

# Compute the average degree connectivity
avg_degree_connectivity = sum(degree[k] for k in set(degree)) / len(G)

print("Average Degree Connectivity: ", avg_degree_connectivity)
