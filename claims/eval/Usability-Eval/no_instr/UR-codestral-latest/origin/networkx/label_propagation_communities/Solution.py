import networkx as nx

# Assume that G is your graph
G = nx.Graph()

# Add nodes and edges to your graph here...
# For example:
# G.add_node('A')
# G.add_edge('A', 'B')

# Perform label propagation
label_propagation = nx.algorithms.community.label_propagation.label_propagation_communities(G)

# Print the community sets
for i, community in enumerate(label_propagation):
    print(f"Community {i}: {community}")
