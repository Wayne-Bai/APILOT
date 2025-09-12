import networkx as nx
from networkx.algorithms.community import label_propagation_communities

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)

# Use label propagation to identify community sets
communities = label_propagation_communities(G)

# Output the community sets
for i, community in enumerate(communities):
    print(f"Community {i+1}: {community}")
