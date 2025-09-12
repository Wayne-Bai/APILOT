import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges (you can add as many edges as you want)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Compute harmonic centrality
harmonic_centrality = nx.harmonic_centrality(G)

# Print the harmonic centrality for each node
for node in G.nodes():
    print(f"The harmonic centrality of node {node} is {harmonic_centrality[node]}")
