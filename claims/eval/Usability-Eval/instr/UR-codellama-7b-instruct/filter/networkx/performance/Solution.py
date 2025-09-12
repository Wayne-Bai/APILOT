import networkx as nx

# Define the graph
G = nx.erdos_renyi_graph(100, 0.1)

# Partition the graph into communities
communities = [2, 4]

# Calculate the number of intra-community edges and inter-community non-edges
intra_community_edges = 0
inter_community_non_edges = 0
for edge in G.edges:
    if communities[edge[0]] == communities[edge[1]]:
        intra_community_edges += 1
    else:
        inter_community_non_edges += 1

# Calculate the total number of potential edges
total_edges = G.number_of_nodes * (G.number_of_nodes - 1) / 2

# Calculate the performance of the partition
performance = (intra_community_edges + inter_community_non_edges) / total_edges
print("Performance:", performance)
