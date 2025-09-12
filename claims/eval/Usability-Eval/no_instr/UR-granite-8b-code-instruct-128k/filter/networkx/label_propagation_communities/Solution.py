import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'F')
G.add_edge('F', 'A')

# Perform label propagation
communities = nx.label_propagation_communities(G)

# Print the community sets
for community in communities:
    print(community)
