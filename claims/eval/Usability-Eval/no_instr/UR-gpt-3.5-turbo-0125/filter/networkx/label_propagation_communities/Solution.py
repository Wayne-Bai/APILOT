
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph...

# Generate community sets determined by label propagation
communities = list(nx.community.label_propagation_communities(G))
print(communities)
