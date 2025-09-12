import networkx as nx
from operator import itemgetter

# Initialize a graph
G = nx.Graph()

# Add edges
# The harmonic centrality of a node u is the sum of the reciprocals of the distances between u and all nodes v in the graph.
# So, we need to ensure there are paths between all pairs of nodes, otherwise harmonic centrality might not be calculable.
G.add_edge('a', 'b')
G.add_edge('b', 'c')
G.add_edge('c', 'd')

# Compute the harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print harmonic centrality of each node
print(harmonic_centrality)
