import networkx as nx

# Assuming 'G' is your graph
G = nx.Graph()

# Add edges to the graph
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')

# Compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

print(harmonic_centrality)
