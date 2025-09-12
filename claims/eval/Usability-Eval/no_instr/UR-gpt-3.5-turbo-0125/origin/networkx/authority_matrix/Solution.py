
import networkx as nx

# Create a graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Calculate the HITS authority matrix
authority_matrix = nx.hits(G, max_iter=100)[1]

print(authority_matrix)
