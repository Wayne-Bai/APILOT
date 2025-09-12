import networkx as nx

# Assuming you have a graph `G` and you want to compute harmonic centrality
G = nx.Graph()

# Example: adding nodes and edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print harmonic centrality for each node
for node in G.nodes():
    print(f"Node {node}: {harmonic_centrality[node]}")
