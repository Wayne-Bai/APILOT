import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

# Compute harmonic centrality for nodes
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality values
for node, centrality in harmonic_centrality.items():
    print(f"Node {node}: {centrality}")
