
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Calculate the HITS authority matrix
authority = nx.hits(G, normalized=True)
print(authority)
