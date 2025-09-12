import networkx as nx

def calculate_partition_performance(graph, partition):
    total_edges = graph.number_of_edges()
    intra_community_edges = 0
    inter_community_non_edges = 0

    for node in graph.nodes():
        node_community = partition[node]
        for neighbor in graph.neighbors(node):
            neighbor_community = partition[neighbor]
            if node_community == neighbor_community:
                intra_community_edges += 1
            else:
                inter_community_non_edges += 1

    partition_performance = (intra_community_edges + inter_community_non_edges) / total_edges
    return partition_performance

# Example usage:
# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Define a partition
partition = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1}

# Calculate partition performance
performance = calculate_partition_performance(G, partition)
print("Partition Performance:", performance)
