import networkx as nx

def partition_coverage_performance(G, partition):
    # Calculate the coverage of the partition
    coverage = sum(len(set(partition[v]) & set(G.neighbors(v))) for v in G.nodes()) / len(G.nodes())

    # Calculate the performance of the partition
    performance = sum(len(set(partition[v]) & set(partition[u])) for v, u in G.edges()) / len(G.edges())

    return coverage, performance

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
partition = {1: {2, 3}, 2: {1, 3, 4}, 3: {1, 2, 4, 5}, 4: {2, 3, 5}, 5: {3, 4}}
coverage, performance = partition_coverage_performance(G, partition)
print(f"Coverage: {coverage}, Performance: {performance}")
