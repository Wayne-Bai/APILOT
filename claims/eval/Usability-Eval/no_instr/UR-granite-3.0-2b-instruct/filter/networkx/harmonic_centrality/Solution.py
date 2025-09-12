import networkx as nx

# Assuming G is your graph
G = nx.Graph()

# Add nodes and edges to your graph

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the results
for node, score in harmonic_centrality.items():
    print(f"Node {node}: {score}")
