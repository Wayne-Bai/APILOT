import networkx as nx

def partition_performance(G, partition):
    intra_edges = 0
    inter_non_edges = 0
    for community in partition:
        for node in community:
            for neighbor in G:
                if node != neighbor:
                    if (neighbor in community) and G.has_edge(node, neighbor):
                        intra_edges += 1
                    elif (neighbor not in community) and not G.has_edge(node, neighbor):
                        inter_non_edges += 1

    total_possible_edges = len(G) * (len(G) - 1) // 2
    performance = (intra_edges + inter_non_edges) / total_possible_edges

    return performance

# Usage Example
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (3, 4)])
partition = [{0, 1, 2}, {3, 4}]
performance = partition_performance(G, partition)
print(f'Partition Performance: {performance}')
