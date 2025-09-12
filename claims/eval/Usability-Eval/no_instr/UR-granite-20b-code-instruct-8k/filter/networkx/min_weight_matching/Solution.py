
import networkx as nx

G = nx.Graph()  # Create an empty graph

# Add edges to the graph with weights
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=5)

# Compute the minimum-weight maximal matching
matching = nx.max_weight_matching(G, True)

# Print the matching
print("Minimum-weight maximal matching:", matching)
