import networkx as nx

# Assuming G is your graph and partition is a list of sets, each representing a partition of G

def partition_metrics(G, partition):
    coverage = [len(part) / G.number_of_nodes() for part in partition]
    performance = [nx.average_node_connectivity(G.subgraph(part)) for part in partition]
    return coverage, performance

# Replace the following lines with your graph and partition
G = nx.Graph()
partition = [{1, 2, 3}, {4, 5, 6}]

coverage, performance = partition_metrics(G, partition)
print(f"Coverage: {coverage}")
print(f"Performance: {performance}")
