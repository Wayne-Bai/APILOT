import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5)])

# Function to calculate harmonic centrality
def harmonic_centrality(G):
    centrality = {}
    for v in G.nodes():
        sum_distances = 0.0
        for u in G.nodes():
            if v!= u:
                try:
                    sum_distances += 1 / nx.shortest_path_length(G, source=v, target=u)
                except nx.NetworkXNoPath:
                    # If there's no path between the nodes, we consider it as a distance of 0
                    pass
        centrality[v] = sum_distances / (len(G.nodes()) - 1)
    return centrality

# Calculate harmonic centrality
centrality = harmonic_centrality(G)

# Print the results
for node in centrality:
    print(f"Harmonic Centrality of node {node}: {centrality[node]}")
