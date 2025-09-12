import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges with weights
G.add_edge(1, 2, weight=0.5)
G.add_edge(1, 3, weight=0.2)
G.add_edge(2, 3, weight=0.8)
G.add_edge(2, 4, weight=0.3)
G.add_edge(3, 4, weight=0.7)

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

print(harmonic_centrality)
