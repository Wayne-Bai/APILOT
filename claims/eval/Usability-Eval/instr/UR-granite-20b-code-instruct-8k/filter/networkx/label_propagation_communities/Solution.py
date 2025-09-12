import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 1)

# Use the label propagation algorithm to determine communities
communities = nx.label_propagation_communities(G)

# Print the communities
for i, community in enumerate(communities):
    print(f'Community {i+1}: {community}')
