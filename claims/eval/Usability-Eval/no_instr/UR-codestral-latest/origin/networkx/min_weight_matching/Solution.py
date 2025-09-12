import networkx as nx
from networkx.algorithms import maximum_matching

# Create a weighted directed graph
G = nx.DiGraph()

# Adding nodes
G.add_nodes_from(["A", "B", "C", "D"])

# Adding weighted edges
G.add_edge("A", "B", weight=2)
G.add_edge("B", "C", weight=3)
G.add_edge("C", "D", weight=1)
G.add_edge("D", "A", weight=4)

# Calculate minimum-weight maximal matching
matching = maximum_matching.max_weight_matching(G, True)

print(matching)
