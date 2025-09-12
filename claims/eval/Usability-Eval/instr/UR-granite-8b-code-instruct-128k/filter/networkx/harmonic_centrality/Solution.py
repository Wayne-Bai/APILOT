import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the results
for node, centrality in harmonic_centrality.items():
    print(f"Node {node}: Harmonic Centrality = {centrality}")
