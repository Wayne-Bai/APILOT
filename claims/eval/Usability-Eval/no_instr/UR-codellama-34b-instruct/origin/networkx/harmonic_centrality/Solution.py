import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Compute harmonic centrality for each node
harmonic_centrality = nx.harmonic_centrality(G)

print("Harmonic centrality:")
for node in G.nodes():
    print(f"{node}: {harmonic_centrality[node]}")
