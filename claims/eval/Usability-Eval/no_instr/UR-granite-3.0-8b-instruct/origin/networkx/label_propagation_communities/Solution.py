import networkx as nx

# Assuming G is your graph
G = nx.Graph()
# Add edges to the graph
G.add_edge('A', 'B', label='friend')
G.add_edge('A', 'C', label='colleague')
G.add_edge('B', 'C', label='colleague')
G.add_edge('B', 'D', label='friend')

# Generate community sets using label propagation
communities = nx.community.label_propagation_communities(G)

# Print the communities
for community in communities:
    print(community)
