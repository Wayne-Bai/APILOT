import networkx as nx
G = nx.Graph()
# Add edges to the graph G
# ...
# Compute the average degree connectivity
avg_degree = nx.average_degree_connectivity(G)
print("Average degree connectivity:", avg_degree)
