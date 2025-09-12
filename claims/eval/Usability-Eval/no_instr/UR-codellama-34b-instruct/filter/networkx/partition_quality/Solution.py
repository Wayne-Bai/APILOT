import networkx as nx
from collections import defaultdict

def get_coverage(G, partitions):
    # Initialize coverage and performance dictionaries
    coverage = defaultdict(int)
    performance = defaultdict(float)

    for partition in partitions:
        # Get the nodes in the current partition
        nodes = set(partition.nodes())

        # Calculate the coverage of the current partition
        coverage[partition] += len(nodes) / len(G.nodes())

        # Calculate the performance of the current partition
        performance[partition] += sum(nx.shortest_path_length(G, source=u, target=v) for u, v in nodes) / len(nodes)

    return coverage, performance
