import networkx as nx
from networkx.algorithms.community import coverage

def partition_cover_and_performance(G):
    partitions = list(nx.algorithms.community.modularity_communities(G))
    partition_cover = coverage(G, partitions)
    partition_performance = sum([p.size*(p.size-1) for p in partition_cover])/(2*G.number_of_edges())
    return partition_cover, partition_performance

# Example usage
G = nx.erdos_renyi_graph(10, 0.5)
cover, performance = partition_cover_and_performance(G)
print(f"Partition Cover: {cover}")
print(f"Partition Performance: {performance}")
