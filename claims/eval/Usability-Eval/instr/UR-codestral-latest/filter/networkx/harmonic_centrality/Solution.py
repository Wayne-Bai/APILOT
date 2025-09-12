import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes in the graph
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Add edges in the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'A')

# Compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

print(harmonic_centrality)
