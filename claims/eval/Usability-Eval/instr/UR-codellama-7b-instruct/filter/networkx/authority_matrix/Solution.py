
import networkx as nx

# Create a directed graph from the edges list
G = nx.DiGraph()
for edge in edges:
    G.add_edge(edge[0], edge[1])

# Compute the HITS authority matrix
auth = nx.hits(G, alpha=0.33, epsilon=0.01)

# Print the HITS authority matrix
print(auth)
