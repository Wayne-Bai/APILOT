
from networkx.algorithms import community
import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5])
G.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (3, 4)])

# Use label propagation algorithm to generate community sets
communities = community.label_propagation_communities(G)

# Print the generated community sets
print(communities)
