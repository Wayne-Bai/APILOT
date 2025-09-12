import networkx as nx

# Create a graph
G = nx.Graph()
# Add nodes and edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Compute the harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality for each node
print("Harmonic Centrality:")
for node, centrality in harmonic_centrality.items():
    print(f"Node {node}: {centrality}")
