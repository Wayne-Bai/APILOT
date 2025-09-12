
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

# Compute a minimum-weight maximal matching of the graph
matching = nx.max_weight_matching(G)

# Print the edges in the matching
for edge in matching:
    print(edge)
