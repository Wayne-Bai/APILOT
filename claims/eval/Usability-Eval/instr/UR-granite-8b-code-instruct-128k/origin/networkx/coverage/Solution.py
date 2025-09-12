
import networkx as nx

def get_coverage(partition):
    graph = partition.graph
    num_edges = graph.number_of_edges()
    num_intra_edges = sum(len(block) - 1 for block in partition.blocks())
    coverage = num_intra_edges / num_edges

    return coverage
