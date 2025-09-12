import networkx as nx
import numpy as np

# Create a random graph for demonstration
G = nx.gnp_random_graph(100, 0.02)

# Create a partition for the graph
partition = {node: np.random.randint(0, 2) for node in G.nodes}

# Calculate the total number of potential edges
total_potential_edges = len(G.nodes) * (len(G.nodes) - 1) / 2

# Calculate the number of intra-community edges
intra_community_edges = 0
for node1 in G.nodes:
    for node2 in G.nodes:
        if partition[node1] == partition[node2] and G.has_edge(node1, node2):
            intra_community_edges += 1

# Calculate the number of inter-community non-edges
inter_community_non_edges = 0
for node1 in G.nodes:
    for node2 in G.nodes:
        if partition[node1] != partition[node2] and not G.has_edge(node1, node2):
            inter_community_non_edges += 1

# Calculate the performance of the partition
performance = (intra_community_edges + inter_community_non_edges) / total_potential_edges
print(f'The performance of the partition is: {performance}')
