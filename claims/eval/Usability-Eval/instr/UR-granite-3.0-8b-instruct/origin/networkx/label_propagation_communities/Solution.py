import networkx as nx
from networkx.algorithms.community import label_propagation_communities

# Assuming G is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])

# Generate community sets using label propagation
communities = label_propagation_communities(G)

print(communities)
