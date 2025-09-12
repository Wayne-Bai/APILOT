import networkx as nx

def partition_performance(G, partition):
    intra_community_edges = 0
    inter_community_edges = 0
    total_potential_edges = 0

    for u in partition:
        for v in partition:
            if u != v:
                total_potential_edges += 1
                if G.has_edge(u, v) and G[u][v]['partition'] == G[u][u]['partition'] + G[v][u]['partition']:
                    intra_community_edges += 1
                elif not G[u][v] and (G[u][u]['partition'] in G[v] or G[v][v]['partition'] in G[u]):
                    inter_community_edges += 1

    performance = (intra_community_edges + inter_community_edges) / total_potential_edges
    return performance

# Example usage
# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)])

# Define a partition
partition = {(1, 2, 3), (4, 5, 6)}

# Compute the partition performance
print(partition_performance(G, partition))
