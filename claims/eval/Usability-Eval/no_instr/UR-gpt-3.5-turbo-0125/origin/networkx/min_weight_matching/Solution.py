
import networkx as nx

G = nx.Graph()

# Add nodes and edges to the graph G

# Find a minimum-weight maximal matching of G
matching = nx.max_weight_matching(G, True)
print(matching)
