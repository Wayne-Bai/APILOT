import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add some edges
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')
G.add_edge('B', 'D')

# Compute the harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality of each node
for node, centrality in harmonic_centrality.items():
    print(f"Harmonic Centrality of {node}: {centrality}")
