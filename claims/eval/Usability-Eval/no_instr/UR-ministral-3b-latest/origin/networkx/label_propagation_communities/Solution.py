import networkx as nx

# Define an example graph
G = nx.Graph()

# Add nodes and edges
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)

# Apply label propagation to find communities
communities = nx.algorithms.community.label_propagation.LabelPropagationCommunity(G).communities()

# Print out the communities
print(communities)
