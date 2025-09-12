
import networkx as nx
# Create a graph
G = nx.Graph()
G.add_edge(1, 2, weight=2)
G.add_edge(1, 3, weight=3)
G.add_edge(2, 3, weight=1)
# Compute a minimum-weight maximal matching
matching = nx.max_weight_matching(G)
# Print the matching
print(matching)
