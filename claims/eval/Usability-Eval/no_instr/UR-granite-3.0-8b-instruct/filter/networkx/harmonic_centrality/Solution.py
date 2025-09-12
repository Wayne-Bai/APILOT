import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality for each node
for node, centrality in harmonic_centrality.items():
    print(f"Node {node}: {centrality}")
